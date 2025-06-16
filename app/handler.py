from models.zero_shot import ZeroShotModel
from models.few_shot import FewShotModel

zero_shot_model = ZeroShotModel()
few_shot_model = FewShotModel()

def get_fine_tuned_model():
    from models.fine_tuned import FineTunedModel
    return FineTunedModel()

def predict(text: str, model_type: str = "zero-shot") -> str:
    if model_type == "few-shot":
        results = few_shot_model.predict(text)
        title = "Few-Shot"
    elif model_type == "fine-tuned":
        results = get_fine_tuned_model().predict(text)
        title = "Fine-Tuned"
    else:
        results = zero_shot_model.predict(text)
        title = "Zero-Shot"

    output = f"### Résultat de la classification ({title}) :\n\n"
    for label, score in results:
        output += f"- **{label}** : {score * 100:.1f}%\n"
    return output