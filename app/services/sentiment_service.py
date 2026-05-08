from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):

    if not text:
        return "UNKNOWN"

    result = sentiment_pipeline(text[:512])

    return result[0]["label"]