import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="FinSight AI",
    layout="wide"
)

st.sidebar.title("FinSight AI")
st.sidebar.write("Real-time financial sentiment tracker")
st.title("📈 FinSight AI Dashboard")

st.subheader("AI-Powered Financial News Sentiment Analysis")

API_URL = "http://127.0.0.1:8000/financial-news"

response = requests.get(API_URL)

data = response.json()

summary = data["sentiment_summary"]

articles = data["articles"]

# ======================
# METRICS
# ======================

col1, col2, col3 = st.columns(3)

col1.metric("🟢 Positive", summary["positive"])

col2.metric("🔴 Negative", summary["negative"])

col3.metric("⚪ Neutral", summary["neutral"])

st.divider()

# ======================
# ARTICLES SECTION
# ======================

st.header("📰 Financial News")

for article in articles:

    sentiment = article["sentiment"]

    if sentiment == "POSITIVE":
        emoji = "🟢"

    elif sentiment == "NEGATIVE":
        emoji = "🔴"

    else:
        emoji = "⚪"

    with st.container():

        st.subheader(article["title"])

        st.write(f"**Source:** {article['source']}")

        st.write(
            f"**Sentiment:** {emoji} {article['sentiment']}"
        )

        st.write(
            f"**Confidence Score:** {article['confidence_score']}"
        )

        st.markdown(
            f"[Read Full Article]({article['url']})"
        )

        st.divider()

# ======================
# DATAFRAME SECTION
# ======================

st.header("📊 Structured Data")

df = pd.DataFrame(articles)

st.dataframe(df)   