import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="FinSight AI",
    layout="wide"
)

st.sidebar.title("FinSight AI")
st.sidebar.title("Filters")
sentiment_filter = st.sidebar.selectbox("Select Sentiment", ["All","positive","negative","neutral"])
search_query = st.sidebar.text_input(
    "Search News"
)
st.sidebar.write("Real-time financial sentiment tracker")
st.title("📈 FinSight AI Dashboard")

st.subheader("AI-Powered Financial News Sentiment Analysis")

API_URL = "http://127.0.0.1:8000/financial-news"

response = requests.get(API_URL)

data = response.json()

summary = data["sentiment_summary"]

articles = data["articles"]

# METRICS

col1, col2, col3 = st.columns(3)

col1.metric("🟢 Positive", summary["positive"])

col2.metric("🔴 Negative", summary["negative"])

col3.metric("⚪ Neutral", summary["neutral"])

st.divider()


# ARTICLES SECTION
st.header("📰 Financial News")
filtered_articles = []
for article in articles:
    matches_sentiment = (
        sentiment_filter == "ALL"
        or article["sentiment"] == sentiment_filter
    )
    matches_search = (
        search_query.lower()
        in article["title"].lower()
    )
    if matches_sentiment and matches_search:
        filtered_articles.append(article)

for article in filtered_articles:
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


# DATAFRAME SECTION
st.header("📊 Sentiment Distribution")

labels = ["Positive", "Negative", "Neutral"]

values = [
    summary["positive"],
    summary["negative"],
    summary["neutral"]
]

plt.rcParams.update({'font.size': 5})
fig, ax = plt.subplots(figsize = (2,2))
colors = ["#80ff00", "#7f00ff", "#f5ebff"]

ax.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    colors=colors,
    startangle = 90
)
ax.axis("equal")
st.pyplot(fig, use_container_width=False)

st.header("📊 Structured Data")
df = pd.DataFrame(articles)
st.dataframe(df)   