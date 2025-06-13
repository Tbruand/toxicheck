from models.base import BaseModel

# Exemple de modèle minimal
class DummyModel(BaseModel):
    def predict(self, text):
        if "stupide" in text.lower():
            return "toxique"
        return "non-toxique"

dummy = DummyModel()

def predict(text: str) -> str:
    return dummy.predict(text)