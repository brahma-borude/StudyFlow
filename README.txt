<p align="center">
    <img width="100" alt="studyflow" src="https://github.com/user-attachments/assets/34433430-0848-47ff-bc72-b68bba6d9a95" />
</p>

#  StudyFlow

StudyFlow is a personal learning dashboard that helps you create, track, and manage mini-courses from YouTube.
It combines Bootstrap UI + Django backend + AI (Groq) to generate structured learning roadmaps.

## Features

- Dashboard with sidebar navigation
- Search bar to enter any topic you want to learn
- Auto-generated mini-courses (20 YouTube videos per topic)
- AI-generated learning roadmap – organizes videos into a logical order
- Bootstrap styling for responsive UI

## 🛠️ Tech Stack

- Frontend: Bootstrap 5, Custom CSS
- Backend: Django 5
- Database: SQLite (default)
- APIs: YouTube Search API (youtubesearchpython)
- AI: Groq LLaMA for roadmap generation

## 📂 Project Structure
```
StudyFlow/
│── apps/
│   └── dashboard/        # Main dashboard app
│── services/
│   ├── youtube_service.py # YouTube search logic
│   └── groq_service.py    # AI roadmap + summarization
│── templates/
│   └── dashboard/         # HTML templates
│── static/
│   └── css/               # Custom CSS
│── manage.py
│── requirements.txt
│── README.md
```
## ⚡ Installation

Clone the repo

```git clone https://github.com/yourusername/studyflow.git
cd studyflow
```

Create & activate a virtual environment
```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

Install dependencies

```pip install -r requirements.txt```


Set environment variables
Create a .env file in the root:
```
YOUTUBE_API_KEY=your_youtube_api_key
GROQ_API_KEY=your_groq_api_key
```

Run migrations
```
python manage.py migrate
```

Start the server
```
python manage.py runserver
```
