import os
import streamlit as st
import google.generativeai as genai

# ---------------------------------------------------
# Load Gemini API key securely
# Priority: Streamlit secrets -> environment variable
# NEVER hardcode your API key here.
# ---------------------------------------------------
api_key = None
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error(
        "⚠️ Gemini API key not found.\n\n"
        "Set it as GEMINI_API_KEY in .streamlit/secrets.toml (local) "
        "or as an environment variable (Colab/other hosts)."
    )
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------------------------------------------
# Page setup
# ---------------------------------------------------
st.set_page_config(page_title="AI Learning Buddy Deekshitha", page_icon="🎓")
st.title("🎓 AI Learning Buddy Deekshitha")
st.caption("Your personal AI-powered study companion, built with Gemini + Streamlit.")

# ---------------------------------------------------
# UI
# ---------------------------------------------------
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything",
    ],
)

if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."
        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."
        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."
        else:
            prompt = topic

        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong while calling Gemini: {e}")
