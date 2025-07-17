import pandas as pd
from chat_insight.formatter import format_chat
from chat_insight.analyzer import analyze_chat
import ast
import json

def test_format_chat():
    data = {
        "message_type": ["user", "chatbot"],
        "received_at": ["2025-07-16 10:00", "2025-07-16 10:01"],
        "message": ["Hello", "Hi, how can I help?"]
    }
    df = pd.DataFrame(data)
    expected_output = (
        "2025-07-16 10:00 - Customer: Hello\n"
        "2025-07-16 10:01 - Bot: Hi, how can I help?"
    )
    assert format_chat(df) == expected_output


def test_analyze_chat_transcript(monkeypatch):
    import json
    from chat_insight import analyzer

    # Fake response JSON string
    fake_data = {
        "is_struggling": True,
        "struggle_reason": "Customer is confused about pricing",
        "sentiment": "negative",
        "summary": "Customer was unhappy with unclear pricing."
    }

    class MockMessage:
        content = json.dumps(fake_data)

    class MockChoice:
        message = MockMessage()

    class MockResponse:
        choices = [MockChoice()]

    class MockCompletion:
        @staticmethod
        def create(*args, **kwargs):
            return MockResponse()

    class MockChat:
        completions = MockCompletion()

    class MockClient:
        chat = MockChat()

    # Replace the actual OpenAI client with the mock
    monkeypatch.setattr(analyzer, "client", MockClient())

    # Run test
    transcript = (
        "2025-07-16 10:00 - Customer: How much does it cost?\n"
        "2025-07-16 10:01 - Bot: It depends on your plan."
    )
    result = analyzer.analyze_chat(transcript)

    # Assertions
    assert result["is_struggling"] is True
    assert result["sentiment"] == "negative"
    assert "pricing" in result["struggle_reason"]
