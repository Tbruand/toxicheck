import gradio as gr
from app.handler import predict

def launch_app():
    iface = gr.Interface(
        fn=predict,
        inputs="text",
        outputs="markdown",
        title="🧪 ToxiCheck",
        description="Entrez un texte pour détecter s'il est toxique. Résultat avec score de confiance pour chaque label."
    )
    iface.launch()