
<p align="center">
  <img height="100px" align='center' alt="studyflow" src="https://github.com/user-attachments/assets/3c22d313-c711-4e81-b185-5dedbfb43fd0" />
</p>

# StudyFlow 

StudyFlow is an **AI-powered learning planner** that helps students stay consistent, organized, and productive while studying. It generates personalized topic-wise roadmaps, fetches relevant learning resources, and tracks progress visually — making studying smarter and more efficient.  


## ✨ Features  

- 🎯 **Personalized Roadmaps** – Enter your learning goals & experience level, and get a tailored roadmap generated using AI.  
- 🎥 **Curated Learning Resources** – Topic-wise YouTube videos fetched automatically.  
  

## 🖼️ Screenshots  
<img  height="240px" alt="Screenshot 2025-08-30 123348" src="https://github.com/user-attachments/assets/ed6983bf-635c-4230-a46f-827e6b47e359" />
<img  height="240px" src="https://github.com/user-attachments/assets/9198956f-22cd-4eaf-bcac-ac6bddd72bf5" />
<img  height="250px" src="https://github.com/user-attachments/assets/1439e06f-e82c-437e-9df4-a1a9527a8292" />
<img  height="250px" src="https://github.com/user-attachments/assets/3a21db6f-f096-4273-951c-78819584a747" />

---

## 🚀 Tech Stack  

- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Django (Python)  
- **Database:** SQLite (can be upgraded to PostgreSQL/MySQL)  
- **APIs:** YouTube Data API (for fetching videos), LLM (for generating roadmaps)  

---

## ⚡ Getting Started  

### 1. Clone the Repository
```bash
git clone https://github.com/brahma-borude/StudyFlow.git
cd StudyFlow
```
### 2. Create Virtual Environment & Install Dependencies
``` bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Environment Variables

To run this project, you will need to add the following environment variables to a `.env` file in the project root:

```env
# YouTube Data API key
YOUTUBE_API_KEY=your_youtube_api_key_here

# Groq API key
GROQ_API_KEY=your_groq_api_key_here
```
### 4️.  Run the Server
``` bash
python manage.py migrate
python manage.py runserver
```

Now open your browser and go to:

👉 http://127.0.0.1:8000/

### 📬 Contact

👨‍💻 Author: Brahma Borude

🔗 LinkedIn: https://www.linkedin.com/in/brahma-borude

💻 GitHub: https://github.com/brahma-borud
