import streamlit as st
import requests

st.set_page_config(
    page_title="FinSight AI",
    layout="wide"
)

st.title("📈 FinSight AI Dashboard")

st.subheader("AI-Powered Financial News Sentiment Analysis")

API_URL = "http://127.0.0.1:8000/financial-news"

response = requests.get(API_URL)

data = response.json()

st.write("### Sentiment Summary")
st.json(data["sentiment_summary"])

st.write("### Financial News Articles")

for article in data["articles"]:

    st.subheader(article["title"])

    st.write(f"Source: {article['source']}")

    st.write(f"Sentiment: {article['sentiment']}")

    st.write(f"Confidence Score: {article['confidence_score']}")

    st.markdown(f"[Read Article]({article['url']})")

    st.divider()