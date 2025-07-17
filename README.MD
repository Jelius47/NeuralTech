
# 🧠 Chat Insight – Identify Struggling Customers via LLMs

**Chat Insight** is a Python package designed to analyze chat conversations (e.g. from support or sales) and detect **customer sentiment**, **struggles**, and generate **summaries** using LLMs (like GPT-4). Ideal for businesses that want to monitor and improve customer experience in real-time.

---

## 🚀 Features

- 🔍 Detect if a customer is struggling.
- 💬 Identify what they’re struggling with.
- 😕 Understand the sentiment (positive, neutral, negative).
- 🧾 Get a concise summary of each chat.
- 📊 Return results as a clean, structured DataFrame.

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chat_insight.git
   cd chat_insight
   ```

2. **Install the package:**

   ```bash
   pip install -e .
   ```

3. **Install dependencies (if not already installed):**

   ```bash
   pip install openai pandas
   ```

---

## 🔑 Prerequisites

* Python 3.8+
* OpenAI API key (required for GPT-based analysis)

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-openai-api-key'
```

Alternatively, if you're using a `.env` loader like `python-dotenv`, you can load it in your script.

---

## 🧪 Example Usage

```python
import pandas as pd
from chat_insight import analyze_all_chats

# Load your chat data
df = pd.read_csv("your_chat_data.csv")

# Required columns: chat_id, message, message_type, received_at, responded_at
# Make sure timestamps are parsed
df['received_at'] = pd.to_datetime(df['received_at'])

# Analyze all chat threads (grouped by chat_id)
results = analyze_all_chats(df, max_messages=40)

# View results
print(results.head())
```

---

## 🧠 What the Output Looks Like

Each row in the result represents one chat thread:

| chat\_id | is\_struggling | struggle\_reason     | sentiment | summary                    |
| -------- | -------------- | -------------------- | --------- | -------------------------- |
| abc123   | True           | Delivery delay issue | Negative  | Customer was frustrated... |
| xyz789   | False          | None                 | Neutral   | General product inquiry... |

---

## 📁 Project Structure

```
chat_insight/
│
├── chat_insight/
│   ├── __init__.py          # Exports main methods
│   ├── analyzer.py          # GPT-based analyzer
│   ├── formatter.py         # Converts chat to readable text
│   └── utils.py             # Batch processing logic
│
├── tests/
│   └── test_analyzer.py     # Basic tests (optional)
│
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🧼 Assumptions

* Only the following columns are considered:
  `chat_id`, `message`, `message_type`, `received_at`, `responded_at`
* Avoid using memory/context-tracking features — this version trims chats to the **last N messages**.
* The chat is sorted by `received_at` timestamp for chronological accuracy.

---

## 📍 Limitations

* GPT-4 context limit (\~8,000 tokens) means extremely long chats will be truncated.
* Requires internet and valid OpenAI API credentials.
* May be slow for large datasets due to LLM latency.

---


## 🙌 Contributing

Pull requests are welcome! If you find bugs or want new features, please open an issue.

---


---

## 👨‍💻 Author

Made with ❤️ by \Jelius Heneriko
```

---

