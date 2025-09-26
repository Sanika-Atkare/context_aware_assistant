# backend/app/agent.py
"""
Very small agent that:
- stores the turn in memory (in-memory for now)
- looks for keywords to call calendar_tool.create_event
- otherwise returns an echo reply
"""
from app import memory
from app.tools.calendar_tool import create_event_stub
from datetime import datetime, timedelta

def handle_user_message(user_id: int, text: str):
    # 1) Save turn to short-term memory
    memory.add_turn(user_id, text)

    # 2) Very naive intent detection
    lowered = text.lower()

    if "schedule" in lowered or "reschedule" in lowered or "meeting" in lowered:
        # For MVP we will parse a few simple phrases by heuristics.
        # Example user input: "Schedule meeting tomorrow at 4pm with Raj"
        # This stub will schedule for tomorrow at 16:00 if we can't parse date.
        # (Replace this with robust parsing or an LLM later.)
        start = datetime.utcnow() + timedelta(days=1)
        start = start.replace(hour=16, minute=0, second=0, microsecond=0)
        end = start + timedelta(hours=1)
        event = create_event_stub(summary=text[:80], start_dt=start, end_dt=end)
        reply = f"OK — scheduled (stub). Title: {event['summary']}. Start: {event['start']}"
        return {"reply": reply, "memory_hits": memory.get_recent(user_id)}

    # default: echo with memory hits
    return {"reply": f"I heard: {text}", "memory_hits": memory.get_recent(user_id)}
