#!/bin/bash

echo "🚀 Lancement du projet ToxiCheck..."

# 1. Active l'environnement virtuel
if [ -d "venv" ]; then
  echo "📦 Activation de l'environnement virtuel..."
  source venv/bin/activate
else
  echo "❌ Aucun environnement virtuel trouvé. Tu peux en créer un avec : python -m venv venv"
  exit 1
fi

# 2. Installation des dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# 3. Vérifie que les hooks sont bien installés
if [ ! -f ".git/hooks/commit-msg" ]; then
  echo "🔧 Installation des hooks Commitizen..."
  cz install
fi

# 4. Lancement de l'app Gradio
echo "🧪 Lancement de l'application Gradio..."
python main.py