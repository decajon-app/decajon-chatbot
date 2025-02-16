import uvicorn
from fastapi import FastAPI
from app.routes.chatbot_router import chatbot_router

app = FastAPI(title = "DeCajón - ChatbotAPI")

app.include_router(chatbot_router, prefix = "/api") 

if __name__ == "__main__":
    uvicorn.run("main:app",
                host = "0.0.0.0",
                port = 8000,
                reload = True)
