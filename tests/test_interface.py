import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.interface import predict

def test_predict_zero_shot():
    result = predict("Tu es gentil.", model_type="zero-shot")
    assert isinstance(result, str)
    assert "Résultat de la classification" in result

def test_predict_few_shot():
    result = predict("Tu es débile.", model_type="few-shot")
    assert isinstance(result, str)
    assert "Résultat de la classification" in result

def test_predict_empty_input():
    try:
        result = predict("", model_type="zero-shot")
    except ValueError as e:
        assert "at least one sequence" in str(e)

def test_predict_invalid_model():
    try:
        predict("Texte test", model_type="unknown")
    except ValueError as e:
        assert "Modèle inconnu" in str(e)

def test_create_interface():
    from app.interface import create_interface
    iface = create_interface()
    assert iface is not None