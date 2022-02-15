import os
import torch
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.models.sentiment import (
    Sentiment,
    SentimentPredictResponse,
    SentimentExplainResponse,
)

# Load .env file
load_dotenv()
COMPUTE_DEVICE = int(os.getenv("COMPUTE_DEVICE"))

# Settings
torch.set_grad_enabled(False)
torch.set_num_threads(1)

limiter = Limiter(key_func=get_remote_address)
# Create app
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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
@limiter.limit("5/minute")
def read_root(request: Request):
    return {"API": "online"}


@app.post("/sentiment", response_model=SentimentPredictResponse)
@limiter.limit("10/minute")
def get_sentiment(text: Text, request: Request):
    return sentiment.predict(text.value)


@app.post("/sentiment/explain", response_model=SentimentExplainResponse)
@limiter.limit("3/minute")
def get_explain(text: Text, request: Request):
    return sentiment.explain(text.value)
