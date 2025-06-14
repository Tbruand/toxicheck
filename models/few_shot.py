from models.base import BaseModel

class FewShotModel(BaseModel):
    def __init__(self):
        self.examples = [
            ("Tu es un abruti", "toxique"),
            ("Je vais te tuer", "toxique"),
            ("Merci pour ton aide", "non-toxique"),
            ("J'apprécie ton soutien", "non-toxique")
        ]

    def predict(self, text: str) -> str:
        text = text.lower()

        # Score simple basé sur correspondance de mots-clés
        toxic_score = sum(any(word in example.lower() for word in text.split()) for example, label in self.examples if label == "toxique")
        non_toxic_score = sum(any(word in example.lower() for word in text.split()) for example, label in self.examples if label == "non-toxique")

        return "toxique" if toxic_score >= non_toxic_score else "non-toxique"