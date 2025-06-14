from models.zero_shot import ZeroShotModel

model = ZeroShotModel()

def predict(text: str) -> str:
    results = model.predict(text)
    output = "### Résultat de la classification :\n\n"
    for label, score in results:
        output += f"- **{label}** : {score*100:.1f}%\n"
    return output