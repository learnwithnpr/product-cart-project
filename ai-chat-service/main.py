from fastapi import FastAPI

from app.routes.chat import router as chat_router


app = FastAPI(
    title="AI Chat API",
    description="Simple FastAPI application with OpenAI integration"
)


app.include_router(
    chat_router,
    prefix="/api"
)


@app.get("/")
def home():
    return {
        "message": "AI Chat API is running"
    }