# backend/app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import handle_user_message

app = FastAPI(title="Context-Aware Assistant (MVP)")

class Message(BaseModel):
    user_id: int
    text: str

@app.post("/api/message")
async def message_endpoint(msg: Message):
    """
    Entrypoint for frontend to send user messages.
    Delegates to agent.handle_user_message which returns a dict.
    """
    result = handle_user_message(msg.user_id, msg.text)
    return result
