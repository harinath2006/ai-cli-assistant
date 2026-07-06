from fastapi import FastAPI, HTTPException

from app.models import ChatRequest, ChatResponse
from app.llm import ask_gemini
from app.logger import logger
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll tighten this later after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI CLI Assistant API is running!"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        logger.info(f"Received prompt: {request.message}")

        response = ask_gemini(request.message)

        logger.info("Gemini response generated successfully")

        return ChatResponse(response=response)

    except Exception as e:
        logger.error(f"Gemini Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Unable to generate response. Please try again later."
        )