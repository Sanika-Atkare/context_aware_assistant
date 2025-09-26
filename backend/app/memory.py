# backend/app/memory.py
"""
Simple in-memory short-term memory store for MVP.
Structure: { user_id: [ {role:'user'|'assistant', 'text':..., 'ts':...}, ... ] }
"""
from collections import defaultdict
from datetime import datetime

_STORE = defaultdict(list)
_MAX_TURNS = 20

def add_turn(user_id: int, text: str, role: str = "user"):
    entry = {"role": role, "text": text, "ts": datetime.utcnow().isoformat()}
    lst = _STORE[user_id]
    lst.append(entry)
    # keep only recent N turns
    if len(lst) > _MAX_TURNS:
        _STORE[user_id] = lst[-_MAX_TURNS:]

def get_recent(user_id: int, limit: int = 5):
    return _STORE.get(user_id, [])[-limit:]
