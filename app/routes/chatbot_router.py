from fastapi import APIRouter, Query
from app.services.chatbot_service import process_command

chatbot_router = APIRouter()

@chatbot_router.get("/chatbot")
def chatbot(command: str = Query(..., description = "Comando del usuario")):
    result = process_command(command)
    return result