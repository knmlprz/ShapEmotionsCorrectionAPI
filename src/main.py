import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.models.sentiment import (
    Sentiment,
    SentimentPredictResponse,
    SentimentExplainResponse,
)

# Load .env file
load_dotenv()
COMPUTE_DEVICE = int(os.getenv('COMPUTE_DEVICE'))


# Create app
app = FastAPI()

# Allow CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure compute device
sentiment = Sentiment(device=COMPUTE_DEVICE)


class Text(BaseModel):
    value: str


@app.get("/health")
def read_root():
    return {"API": "online"}


@app.post("/sentiment", response_model=SentimentPredictResponse)
def get_sentiment(text: Text):
    return sentiment.predict(text.value)


@app.post("/sentiment/explain", response_model=SentimentExplainResponse)
def get_explain(text: Text):
    return sentiment.explain(text.value)
