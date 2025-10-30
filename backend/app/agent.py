memory = {}

def handle_user_message(user_id: int, text: str):
    """
    Handles user messages with simple context memory.
    """

    user_history = memory.get(user_id, [])

    # Save current message
    user_history.append({"role": "user", "text": text})
    memory[user_id] = user_history

    # Simple logic
    text_lower = text.lower()

    # 1️⃣ Schedule meeting
    if "schedule" in text_lower and "meeting" in text_lower:
        reply = "✅ Meeting scheduled for tomorrow at 4:00 PM."
    
    # 2️⃣ Remember user's name
    elif "my name is" in text_lower:
        name = text.split("is")[-1].strip().capitalize()
        memory[user_id].append({"role": "system", "name": name})
        reply = f"Nice to meet you, {name}!"
    
    # 3️⃣ Recall last question
    elif "last question" in text_lower:
        prev_msgs = [m["text"] for m in user_history if m["role"] == "user"]
        if len(prev_msgs) > 1:
            reply = f"Your last question was: '{prev_msgs[-2]}'"
        else:
            reply = "I don’t remember any previous question yet."
    
    # 4️⃣ Default response
    else:
        reply = f"I heard: {text}"

    # Save assistant reply
    memory[user_id].append({"role": "assistant", "text": reply})

    return {"reply": reply, "memory_hits": user_history}
