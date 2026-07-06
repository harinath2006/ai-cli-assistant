# AI CLI Assistant 🤖

A production-style AI Assistant built with Python, FastAPI, Docker, and Google's Gemini API.

## Features

- Interactive AI chat
- FastAPI REST API
- Swagger documentation
- Environment variable management
- Logging
- Error handling
- Unit testing with pytest
- Docker support

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- Docker
- Git & GitHub
- Pytest

## Project Structure

```
app/
    api.py
    config.py
    llm.py
    logger.py
    models.py
    utils.py

tests/

Dockerfile
requirements.txt
README.md
```

## Run Locally

```bash
python -m app.main
```

## Run API

```bash
uvicorn app.api:app --reload
```

## Docker

Build

```bash
docker build -t ai-api .
```

Run

```bash
docker run -p 8000:8000 --env-file .env ai-api
```

## API Docs

```
http://localhost:8000/docs
```

## Future Improvements

- React frontend
- Authentication
- Chat history
- Database
- Streaming responses
