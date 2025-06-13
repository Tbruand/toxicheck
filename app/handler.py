from models.zero_shot import ZeroShotModel

model = ZeroShotModel()

def predict(text: str) -> str:
    return model.predict(text)