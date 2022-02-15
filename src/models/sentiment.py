"""
This module is used to detect sentiment of text and mark why model marked
this text as positive/negative. `cardiffnlp/twitter-roberta-base-sentiment`
from Huggingface is the default model.
"""
import shap
import json
from typing import Tuple, Dict, List
from transformers import pipeline
from pydantic import BaseModel


MODEL = "distilbert-base-uncased-finetuned-sst-2-english"


class SentimentPredictResponse(BaseModel):
    label: str
    score: float


class SentimentExplainResponse(BaseModel):
    text: List[str]
    negative: List[float]
    positive: List[float]


class Sentiment:
    def __init__(self, task="text-classification", model=MODEL, device=-1):
        """

        Parameters
        ----------
        task : str, default="text-classification"
            Task type
        model : str, default="cardiffnlp/twitter-roberta-base-sentiment"
            Model name
        device : int, default=-1 (CPU)
            Device to run model on. To use gpu, check torch.cuda.device_count()
        """
        self.task = task
        self.model = model
        self.device = device
        # This can take a long time to run
        self.pipeline = pipeline(task, model=self.model, device=self.device)
        self.explainer = shap.Explainer(self.pipeline)

    def __translate_result(self, label: str):
        t = {"NEGATIVE": "negative", "POSITIVE": "positive"}
        return t[label]

    def predict(self, data: str) -> SentimentPredictResponse:
        result = self.pipeline(data)
        label = self.__translate_result(result[0]["label"])
        score = result[0]["score"]
        return SentimentPredictResponse(label=label, score=score)

    def explain(self, data: str) -> SentimentExplainResponse:
        labels = ["negative", "positive"]
        shapley_values = self.explainer([data])

        res = {"text": shapley_values.data[0].tolist()}
        for i, label in enumerate(labels):
            res[label] = shapley_values.values[0, :, i].tolist()

        return SentimentExplainResponse.parse_raw(json.dumps(res))


if __name__ == "__main__":
    Sentiment()
