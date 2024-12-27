import streamlit as st
from transformers import pipeline

st.title("Simple Streamlit Demo: Sentiment Analysis")
st.write("This app uses a pre-trained Hugging Face model to analyze the sentiment of the given text.")

# Load Sentiment Analysis Pipeline
pipeline = pipeline("sentiment-analysis")

# Input Text
input_text = st.text_area("Enter text to analyze:", placeholder="Type something here...")

# Analyze Button
if st.button("Analyze Sentiment"):
    if input_text.strip():
        with st.spinner("Analyzing sentiment..."):
            results = sentiment_pipeline(input_text)
        
        # Display Results
        st.subheader("Results:")
        for result in results:
            st.write(f"**Label:** {result['label']}, **Confidence:** {result['score']:.2f}")
    else:
        st.error("Please enter some text to analyze.")
