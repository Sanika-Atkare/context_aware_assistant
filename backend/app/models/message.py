# backend/app/models/message.py
from pydantic import BaseModel

class Message(BaseModel):
    user_id: int
    text: str
