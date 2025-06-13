import gradio as gr
from app.handler import predict

def launch_app():
    iface = gr.Interface(
        fn=predict,
        inputs="text",
        outputs="label",
        title="🧪 ToxiCheck",
        description="Entrez un texte pour détecter s'il est toxique."
    )
    iface.launch()