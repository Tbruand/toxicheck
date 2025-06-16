from transformers import pipeline
from models.base import BaseModel

class ZeroShotModel(BaseModel):
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def predict(self, text: str) -> list[tuple[str, float]]:
        labels = ["toxique", "non-toxique"]
        result = self.classifier(text, candidate_labels=labels)
        return list(zip(result["labels"], result["scores"]))