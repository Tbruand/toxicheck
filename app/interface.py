import gradio as gr
from app.handler import predict, model

def predict(text: str) -> str:
    label, score = model.predict(text)
    return f"{label} ({score*100:.1f}%)"


def launch_app():
    iface = gr.Interface(
        fn=predict,
        inputs="text",
        outputs="text",
        title="🧪 ToxiCheck",
        description="Entrez un texte pour détecter s'il est toxique. Résultat avec score de confiance."
    )
    iface.launch()