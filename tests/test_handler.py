from app.handler import predict

def test_prediction_output():
    result = predict("Tu es stupide")
    assert result in ["toxique", "non-toxique"]