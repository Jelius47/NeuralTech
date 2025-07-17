def format_chat(chat_df, max_messages=40):
    """Format the last N messages of a chat as a text transcript."""
    chat_df = chat_df.sort_values("received_at").tail(max_messages)
    lines = []
    for _, row in chat_df.iterrows():
        sender = "Customer" if row.get('message_type') != 'chatbot' else "Bot"
        lines.append(f"{row['received_at']} - {sender}: {row['message']}")
    return "\n".join(lines)
