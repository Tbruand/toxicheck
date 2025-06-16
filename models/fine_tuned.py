from transformers import CamembertTokenizer, CamembertForSequenceClassification
import torch

class FineTunedModel:
    def __init__(self):
        model_id = "ymokay/toxicheck-camembert"
        self.tokenizer = CamembertTokenizer.from_pretrained(model_id)
        self.model = CamembertForSequenceClassification.from_pretrained(model_id)
        self.model.eval()
        self.label_map = {
            "LABEL_0": "non-toxique",
            "LABEL_1": "toxique"
        }

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
            probs = torch.softmax(logits, dim=1).squeeze()

        labels = [self.label_map.get(self.model.config.id2label[i], self.model.config.id2label[i]) for i in range(len(probs))]
        return [(label, float(probs[i])) for i, label in enumerate(labels)]