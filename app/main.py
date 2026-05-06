from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FinSight AI Backend Running"}

@app.get("/market-status")
def market_status():
    return {
        "market": "US Stocks",
        "sentiment": "Neutral",
        "status": "API working"
    }