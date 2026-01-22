import streamlit as st
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download('stopwords')

st.set_page_config(page_title="NLP Text Preprocessing", layout="centered")

st.title("🧹 NLP Text Preprocessing App")
st.write("Remove HTML tags, punctuation, numbers, stopwords, emojis & extra spaces")

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)

    # Remove emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        "]+",
        flags=re.UNICODE
    )
    text = emoji_pattern.sub(r'', text)

    # Remove numbers
    text = re.sub(r'\d+', ' ', text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in text.split() if w not in stop_words]

    return " ".join(words)

# Text input
user_text = st.text_area("✍️ Enter messy text here:", height=250)

if st.button("Clean Text 🚀"):
    if user_text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        cleaned = clean_text(user_text)
        st.subheader("✅ Cleaned Text")
        st.success(cleaned)
