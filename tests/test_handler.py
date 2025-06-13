import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.handler import predict

def test_zero_shot_prediction_output():
    text_1 = "Tu es complètement stupide"
    text_2 = "Je te remercie pour ton aide"
    
    label_1, score_1 = predict(text_1)
    label_2, score_2 = predict(text_2)

    print(f"Prediction 1: {label_1} ({score_1:.2f})")
    print(f"Prediction 2: {label_2} ({score_2:.2f})")

    assert label_1 in ["toxique", "non-toxique"]
    assert label_2 in ["toxique", "non-toxique"]