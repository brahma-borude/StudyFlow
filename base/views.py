from django.shortcuts import render
from groq import Groq
import requests
from django.conf import settings
from .models import CachedVideo
from django.utils.timezone import now, timedelta

USE_MOCK = False # set to False to use real API



YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
client = Groq(api_key=settings.GROQ_API_KEY)

def dashboard(request):
    return render(request, "base/dashboard.html")


def fetch_youtube_videos(query):
    
    if USE_MOCK:
        return [
        {
            "title": f"Intro to {query}",
            "videoId": "dQw4w9WgXcQ",  # Sample YouTube ID
            "url": f"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/mqdefault.jpg"
        },
        {
            "title": f"{query} Tutorial for Beginners",
            "videoId": "9bZkp7q19f0",
            "url": f"https://www.youtube.com/watch?v=9bZkp7q19f0",
            "thumbnail": "https://img.youtube.com/vi/9bZkp7q19f0/mqdefault.jpg"
        },
        {
            "title": f"Advanced {query} Techniques",
            "videoId": "3JZ_D3ELwOQ",
            "url": f"https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
            "thumbnail": "https://img.youtube.com/vi/3JZ_D3ELwOQ/mqdefault.jpg"
        },
    ]

    cached = CachedVideo.objects.filter(query=query).first()
    if cached:
        # Optional: refresh after 7 days
        if cached.created_at > now() - timedelta(days=7):
            return cached.videos  

    # If not cached or expired → call YouTube API
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 8,
        "key": YOUTUBE_API_KEY,
    }
    response = requests.get(url, params=params).json()

    videos = []
    for item in response.get("items", []):
        videos.append({
            "title": item["snippet"]["title"],
            "videoId": item["id"]["videoId"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
        })

    # Save to DB for later use
    CachedVideo.objects.update_or_create(
        query=query,
        defaults={"videos": videos, "created_at": now()}
    )

    return videos

def create_course(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        stage = request.POST.get("stage")
        plan_name = request.POST.get("plan_name")

        prompt = f"""
        You are an expert curriculum designer.  
        Create a practical, step-by-step learning plan for the topic: "{topic}".  
        Difficulty level: {stage}.  
        Rules:
        1. Each step must be clear, specific, and teachable with existing YouTube videos.  
        2. Avoid abstract or vague steps. Each step should be a concrete concept, tool, or technique that has tutorials on YouTube.  
        3. Output only a numbered list of short step titles (max 6 words).  
        4. Do not include explanations, just the step titles. 
        5. Ensure the steps topics are in youtube. 
        6. Each step should build on the previous one, creating a logical learning progression.  
        7. Limit the plan to 5 steps.
        Example format:
        1. Introduction to {topic}  
        2. Core Concepts of {topic}  
        3. Hands-on with {topic}  
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  
            messages=[{"role": "user", "content": prompt}]
        )

        raw_steps = response.choices[0].message.content.strip()
        
        steps = [line.split(". ", 1)[-1] for line in raw_steps.split("\n") if line.strip()]

        courses = []
        for step in steps:
            query = f'"{step}"'
            videos = fetch_youtube_videos(query)
            courses.append((step, videos))

        context = {
            "plan_name": plan_name,
            "topic": topic,
            "stage": stage,
            "courses": courses
        }

        return render(request, "base/course-result.html", context)

    return render(request, "base/course_form.html")
