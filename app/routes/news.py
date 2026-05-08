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

    for article in articles[:5]:
        title  = article.get("title")
        sentiment = analyze_sentiment(title)

    cleaned_articles.append({
        "title": title,
        "source": article.get("source", {}).get("name"),
        "url": article.get("url"),
        "sentiment": sentiment
    })
    return {
        "status": "success",
        "articles": cleaned_articles
    }