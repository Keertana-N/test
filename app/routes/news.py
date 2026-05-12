from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv
from app.services.sentiment_service import analyze_sentiment
load_dotenv()
router = APIRouter()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@router.get("/financial-news")
def get_financial_news():

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category=business&language=en&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])

    cleaned_articles = []


    positive_count = 0
    negative_count = 0
    neutral_count = 0
    for article in articles[:5]:
        title  = article.get("title")
        sentiment_data = analyze_sentiment(title)
        if sentiment_data["label"] == "POSITIVE":
            positive_count += 1
        elif sentiment_data["label"] == "NEGATIVE":
            negative_count += 1
        else:
            neutral_count += 1

    cleaned_articles.append({
    "title": title,
    "source": article.get("source", {}).get("name"),
    "url": article.get("url"),
    "sentiment": sentiment_data["label"],
    "confidence_score": sentiment_data["score"]
})
    return {
    "status": "success",
    "total_articles": len(cleaned_articles),
    "sentiment_summary": {
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count
    },
    "articles": cleaned_articles
}