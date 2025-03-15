from fastapi import APIRouter, Query
from app.services.chatbot_service import process_command
from app.models.chatbot_request import Request

chatbot_router = APIRouter()

@chatbot_router.get("/chatbot")
def chatbot(request: Request):
    result = process_command(request.command)
    return result
