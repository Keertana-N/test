from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):

    if not text:
        return {
            "label": "UNKNOWN",
            "score": 0
        }

    result = sentiment_pipeline(text[:512])[0]

    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }