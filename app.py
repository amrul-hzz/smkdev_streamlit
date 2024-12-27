import streamlit as st
from transformers import pipeline

st.title("Simple Streamlit Demo: Sentiment Analysis")
st.write("This app uses a pre-trained Hugging Face model to analyze the sentiment of the given text.")

# Load Sentiment Analysis Pipeline
pipeline = pipeline("sentiment-analysis")

# Create two columns
col1, col2 = st.columns(2)

# Input Text in Column 1
with col1:
    input_text = st.text_area("Enter text to analyze:", placeholder="Type something here...")

# Analyze Button and Results in Column 2
with col2:
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
