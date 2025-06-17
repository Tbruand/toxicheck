---
title: ToxiCheck
emoji: 🧪
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 4.25.0
app_file: main.py
pinned: false
---

# 🧪 ToxiCheck — Détection de commentaires toxiques en français

ToxiCheck est une interface Gradio qui permet de détecter automatiquement la toxicité d’un texte en français à l’aide d’un modèle **CamemBERT** fine-tuné.

Ce projet intègre :
- Une interface utilisateur interactive (via Gradio),
- Deux onglets : `Documentation` & `Inférence`,
- Un pipeline NLP complet : tokenizer, prédiction, interprétation.

---

## 🔗 Modèle utilisé

Modèle hébergé sur Hugging Face :  
👉 [ymokay/toxicheck-camembert](https://huggingface.co/ymokay/toxicheck-camembert)

---

## ⚙️ Technologies

- 🧠 Transformers (CamemBERT)
- 🖼️ Gradio
- 🧪 PyTorch
- 🐍 Python 3.10

---

## 🛠️ Lancement local

```bash
git clone https://github.com/Tbruand/toxicheck.git
cd toxicheck
pip install -r requirements.txt
python main.py