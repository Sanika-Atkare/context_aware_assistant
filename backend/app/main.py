# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ---- CORS setup ----
origins = [
    "http://localhost:3000",  # frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Request/Response Model ----
class MessageRequest(BaseModel):
    user_message: str

class MessageResponse(BaseModel):
    reply: str

# ---- Memory storage ----
meetings = []
chat_history = []
user_name = None

@app.post("/api/message", response_model=MessageResponse)
async def get_message(request: MessageRequest):
    global user_name
    user_msg = request.user_message.strip()
    user_msg_lower = user_msg.lower()
    reply = ""

    # Store the user message in chat history
    chat_history.append(user_msg)

    # ----- Detect name -----
    if "my name is" in user_msg_lower:
        # Extract only the actual name after "my name is"
        user_name = user_msg_lower.split("my name is")[-1].strip().title()
        reply = f"Nice to meet you, {user_name}!"

    # ----- Last question -----
    elif "what was my last question" in user_msg_lower or "what is my last question" in user_msg_lower:
        if len(chat_history) >= 2:
            last_question = chat_history[-2]  # previous message
            reply = f"Your last question was: \"{last_question}\""
        else:
            reply = "You haven't asked anything before."

    # ----- Schedule meeting -----
    elif "schedule" in user_msg_lower and "meeting" in user_msg_lower:
        time_info = user_msg_lower.split("on")[-1].strip() if "on" in user_msg_lower else "unspecified time"
        meetings.append(f"Meeting: {time_info}")
        reply = f"✅ Meeting scheduled for {time_info}."

    # ----- Show meetings -----
    elif "show my meetings" in user_msg_lower or "list my meetings" in user_msg_lower:
        if meetings:
            reply = "📅 Your meetings:\n" + "\n".join(meetings)
        else:
            reply = "📅 You have no meetings scheduled."

    # ----- Default friendly reply -----
    else:
        reply = f"You said: \"{user_msg}\"" if user_name else f"Hello! You said: \"{user_msg}\""

    return MessageResponse(reply=reply)
