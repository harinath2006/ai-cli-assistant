# 🤖 AI CLI Assistant

A full-stack AI Assistant built using **Python**, **FastAPI**, **Google Gemini AI**, **React**, **Docker**, and **GitHub Actions**.

This project started as a Command Line Interface (CLI) application and was later converted into a REST API with a React frontend, demonstrating a complete AI application development workflow.

---

## 🚀 Live Demo

### Frontend
> Add your Vercel URL here

Example:

```
https://ai-cli-assistant.vercel.app/
```

### Backend API

> Add your Render URL here

Example:

```
https://ai-cli-assistant.onrender.com
```


# 📌 Features

- 🤖 AI Chat using Google Gemini
- ⚡ FastAPI REST API
- 🎨 React Frontend
- 🐳 Dockerized Backend
- 🔒 Environment Variable Management
- 📝 Logging
- ❌ Error Handling
- ✅ Unit Testing using Pytest
- 🎭 Mock Testing
- 🔄 GitHub Actions CI
- ☁️ Deployment using Render & Vercel

---

# 🏗️ Tech Stack

## Backend

- Python
- FastAPI
- Google Gemini API
- Uvicorn

## Frontend

- React
- Vite
- Axios

## DevOps

- Docker
- Git
- GitHub
- GitHub Actions
- Render
- Vercel

---

# 📂 Project Structure

```
ai-cli-assistant
│
├── app
│   ├── api.py
│   ├── config.py
│   ├── llm.py
│   ├── logger.py
│   ├── models.py
│   ├── utils.py
│   └── main.py
│
├── tests
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .github
    └── workflows
```

---

# 🏛️ Architecture

```
                Browser
                   │
                   ▼
          React Frontend (Vercel)
                   │
              HTTP Request
                   │
                   ▼
         FastAPI Backend (Render)
                   │
                   ▼
          Google Gemini API
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <your-repository-url>
```

Move into the project

```bash
cd ai-cli-assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=your_api_key
APP_NAME=AI CLI Assistant
```

---

# ▶️ Run the Backend

```bash
uvicorn app.api:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 💻 Run the Frontend

Move into frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Open

```
http://localhost:5173
```

---

# 🐳 Docker

Build

```bash
docker build -t ai-cli-assistant .
```

Run

```bash
docker run -p 8000:8000 --env-file .env ai-cli-assistant
```

---

# 🧪 Running Tests

```bash
pytest
```

---


# 🔮 Future Improvements

- Chat History
- User Authentication
- Database Integration
- Streaming Responses
- Dark Mode
- Markdown Rendering
- File Upload
- Conversation Memory

---

# 👨‍💻 Author

**Harinath Gadiyaram**

GitHub:
https://github.com/harinath2006

---

# 📜 License

This project is licensed under the MIT License.