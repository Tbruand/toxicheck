from transformers import pipeline
from models.base import BaseModel

class ZeroShotModel(BaseModel):
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def predict(self, text: str) -> tuple[str, float]:
        labels = ["toxique", "non-toxique"]
        result = self.classifier(text, candidate_labels=labels)
        label = result["labels"][0]
        score = result["scores"][0]
        return label, score