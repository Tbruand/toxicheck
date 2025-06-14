from models.zero_shot import ZeroShotModel
from models.few_shot import FewShotModel

zero_shot_model = ZeroShotModel()
few_shot_model = FewShotModel()

def predict(text: str, model_type: str = "zero-shot") -> str:
    if model_type == "few-shot":
        label = few_shot_model.predict(text)
        return f"### Résultat de la classification (Few-Shot) :\n\n- **{label}**"
    else:
        results = zero_shot_model.predict(text)
        output = "### Résultat de la classification (Zero-Shot) :\n\n"
        for label, score in results:
            output += f"- **{label}** : {score*100:.1f}%\n"
        return output