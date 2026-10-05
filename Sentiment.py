import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="Sentiment AI",
    page_icon="😊"
)

st.title("😊 Sentiment Analysis")
st.write("Analyze the sentiment of any text using AI.")

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

text = st.text_area(
    "Enter your text",
    placeholder="Example: I really enjoyed this movie!"
)

if st.button("🔍 Analyze Sentiment"):

    if text.strip():

        try:
            result = client.text_classification(
                text,
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
            )[0]

            score = result["score"] * 100

            if result["label"] == "POSITIVE":
                st.success(f" Positive — {score:.2f}%")
            else:
                st.error(f" Negative — {score:.2f}%")

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter some text.")