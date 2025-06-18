import gradio as gr
from app.handler import predict

markdown_doc_fr = """
# 📘 Documentation du modèle ToxiCheck

Ce modèle détecte automatiquement la toxicité des commentaires en français à l’aide de variantes de CamemBERT.

---

### 📊 Performances
- Précision (non toxique) : 0.93
- Rappel (non toxique) : 0.93
- F1-score (non toxique) : 0.93

- Précision (toxique) : 0.62
- Rappel (toxique) : 0.61
- F1-score (toxique) : 0.61

- Accuracy globale : 0.88

---

### ⚙️ Types de modèles disponibles
- `zero-shot` : modèle générique sans entraînement spécifique
- `few-shot` : modèle avec apprentissage partiel
- `fine-tuned` : modèle CamemBERT entraîné sur un corpus annoté

---

### 🔗 Modèle utilisé
[ymokay/toxicheck-camembert](https://huggingface.co/ymokay/toxicheck-camembert)
"""

markdown_doc_en = """
# 📘 ToxiCheck Model Documentation

This model automatically detects toxic comments in French using variants of CamemBERT.

---

### 📊 Performance
- Precision (non-toxic): 0.93
- Recall (non-toxic): 0.93
- F1-score (non-toxic): 0.93

- Precision (toxic): 0.62
- Recall (toxic): 0.61
- F1-score (toxic): 0.61

- Overall accuracy: 0.88

---

### ⚙️ Available model types
- `zero-shot`: general-purpose model without specific training
- `few-shot`: model trained on a few examples
- `fine-tuned`: CamemBERT model trained on an annotated corpus

---

### 🔗 Model used
[ymokay/toxicheck-camembert](https://huggingface.co/ymokay/toxicheck-camembert)
"""

def create_interface():
    with gr.Blocks() as demo:
        with gr.Tabs():
            with gr.TabItem("📘 Documentation"):
                lang_selector = gr.Radio(["fr", "en"], label="Langue / Language", value="fr")
                doc_output = gr.Markdown()

                def show_doc(lang):
                    return markdown_doc_fr if lang == "fr" else markdown_doc_en

                lang_selector.change(fn=show_doc, inputs=lang_selector, outputs=doc_output)

            with gr.TabItem("🧪 Inférence"):
                gr.Markdown("### Analyse d'un texte")
                input_text = gr.Textbox(label="Texte à analyser")
                model_choice = gr.Dropdown(choices=["zero-shot", "few-shot", "fine-tuned"], label="Type de modèle", value="zero-shot")
                output = gr.Markdown()
                button = gr.Button("Analyser")
                button.click(fn=predict, inputs=[input_text, model_choice], outputs=output)

    return demo

def launch_app():
    iface = create_interface()
    iface.launch()