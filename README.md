# 🎓 AI Learning Buddy Deekshitha

An AI-powered study companion built with **Streamlit** and **Google Gemini**. Enter any topic and:

- 📖 Get a beginner-friendly explanation
- 🌍 See a real-life example
- 📝 Generate a 5-question quiz with answers
- 💬 Ask it anything

Originally built and run from **Google Colab** using **ngrok** to expose the Streamlit app publicly.

---

## 🚀 Features

| Activity | What it does |
|---|---|
| Explain Concept | Explains the topic in simple language for beginners |
| Real-Life Example | Gives one practical, real-world example |
| Generate Quiz | Creates 5 MCQs with answers on the topic |
| Ask Anything | Sends your topic/question directly to Gemini |

---

## 📁 Project Structure

```
ai-learning-buddy/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── secrets.toml.example        # Template for your API key (copy, don't commit real one)
├── .gitignore
└── README.md
```

---

## 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in and click **Create API Key**
3. Copy the key — you'll use it below

> ⚠️ **Never hardcode your API key in `app.py` or commit it to GitHub.** Public repos get scanned by bots that harvest exposed keys within minutes.

---

## 💻 Option 1: Run Locally

```bash
git clone https://github.com/<your-username>/ai-learning-buddy.git
cd ai-learning-buddy
pip install -r requirements.txt
```

Create your local secrets file:

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edit `.streamlit/secrets.toml` and paste your real key:

```toml
GEMINI_API_KEY = "your-actual-key-here"
```

Run the app:

```bash
streamlit run app.py
```

---

## ☁️ Option 2: Run on Google Colab + ngrok

This is the original setup this project was built for.

**Step 1 — Install dependencies (in a Colab cell):**

```python
!pip install streamlit pyngrok google-generativeai -q
```

**Step 2 — Upload `app.py`** to your Colab session (drag-and-drop into the Files pane, or clone the repo):

```python
!git clone https://github.com/<your-username>/ai-learning-buddy.git
%cd ai-learning-buddy
```

**Step 3 — Set your API key and ngrok authtoken as environment variables:**

```python
import os
os.environ["GEMINI_API_KEY"] = "your-actual-gemini-key"

from pyngrok import ngrok
ngrok.set_auth_token("your-ngrok-authtoken")  # from https://dashboard.ngrok.com/get-started/your-authtoken
```

**Step 4 — Launch Streamlit in the background and expose it via ngrok:**

```python
public_url = ngrok.connect(8501)
print("Your app is live at:", public_url)

!streamlit run app.py &>/content/logs.txt &
```

Click the printed URL to open your AI Learning Buddy in the browser.

> 💡 Colab sessions are temporary — the ngrok URL changes every time you restart, and the free ngrok tier may show an interstitial warning page the first time a visitor opens the link.

---

## 🔒 Security Notes

- API keys belong in `.streamlit/secrets.toml` (local) or environment variables (Colab) — **never** in `app.py`.
- `.streamlit/secrets.toml` is already excluded via `.gitignore`, so it won't be committed.
- If a key is ever accidentally exposed (committed, pasted in chat, etc.), regenerate it immediately in Google AI Studio.

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — web app framework
- [Google Gemini API](https://ai.google.dev/) — `gemini-2.5-flash` model
- [ngrok](https://ngrok.com/) — tunneling for Colab-hosted apps

---

## 📄 License

Feel free to use, modify, and share this project.
