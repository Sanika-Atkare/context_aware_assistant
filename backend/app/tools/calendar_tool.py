# backend/app/tools/calendar_tool.py
"""
Calendar tool (MVP stub).
Place your real Google Calendar integration here later.
This stub simply returns a pretend event dict so you can test flows without OAuth.
"""

def create_event_stub(summary: str, start_dt, end_dt):
    # start_dt and end_dt are datetime objects
    return {
        "id": "stub-event-1",
        "summary": summary,
        "start": start_dt.isoformat(),
        "end": end_dt.isoformat(),
        "status": "confirmed",
    }
