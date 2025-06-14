import gradio as gr
from app.handler import predict

def create_interface():
    return gr.Interface(
        fn=predict,
        inputs=[
            gr.Textbox(label="Texte à analyser"),
            gr.Dropdown(choices=["zero-shot", "few-shot"], label="Type de modèle", value="zero-shot")
        ],
        outputs="markdown",
        title="🧪 ToxiCheck",
        description="Entrez un texte pour détecter s'il est toxique. Résultat avec score de confiance pour chaque label."
    )

def launch_app():
    iface = create_interface()
    iface.launch()