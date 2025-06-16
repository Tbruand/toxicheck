import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.handler import predict

def test_zero_shot_prediction_output():
    text = "Tu es complètement stupide"
    output = predict(text)

    print("Résultat brut :", output)

    # Vérifie que le format markdown est respecté
    assert "### Résultat de la classification" in output
    assert "**toxique**" in output
    assert "**non-toxique**" in output
    assert "%" in output

def test_few_shot_prediction_output():
    from app.handler import predict
    text = "Tu es un abruti fini"
    output = predict(text, model_type="few-shot")

    print("Résultat few-shot :", output)

    assert "### Résultat de la classification" in output
    assert "toxique" in output or "non-toxique" in output

def test_fine_tuned_prediction_output():
    text = "Tu es stupide"
    output = predict(text, model_type="fine-tuned")

    print("Résultat fine-tuned :", output)

    assert "### Résultat de la classification" in output
    assert "toxique" in output or "non-toxique" in output
