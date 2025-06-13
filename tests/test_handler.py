import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.handler import predict

def test_zero_shot_prediction_output():
    text_1 = "Tu es complètement stupide"
    text_2 = "Je te remercie pour ton aide"
    
    output_1 = predict(text_1)
    output_2 = predict(text_2)

    print(f"Prediction 1: {output_1}")
    print(f"Prediction 2: {output_2}")

    assert output_1 in ["toxique", "non-toxique"]
    assert output_2 in ["toxique", "non-toxique"]