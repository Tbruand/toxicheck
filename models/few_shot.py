from models.base import BaseModel
from transformers import pipeline

class FewShotModel(BaseModel):
    def __init__(self):
        # On utilise un modèle préentraîné pour la classification de texte
        self.classifier = pipeline("text-classification", model="textattack/roberta-base-rotten-tomatoes")

    def predict(self, text: str) -> list[tuple[str, float]]:
        result = self.classifier(text, truncation=True)[0]
        label = result["label"].lower()
        score = result["score"]
        label = "non-toxique" if "pos" in label else "toxique"
        return [(label, score)]