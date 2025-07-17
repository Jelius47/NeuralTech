# chat_insight/utils.py
# import pandas as pd
from .formatter import format_chat
from .analyzer import analyze_chat

def analyze_all_chats(df, max_messages=40):
    """Analyze chats grouped by chat_id and return a DataFrame of results."""
    results = []
    grouped_chats = df.sort_values('received_at').groupby('chat_id')
    
    for chat_id, chat_df in grouped_chats:
        transcript = format_chat(chat_df, max_messages=max_messages)
        analysis = analyze_chat(transcript)
        results.append({"chat_id": chat_id, **analysis})
    
    return results
