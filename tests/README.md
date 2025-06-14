## ✅ Tests unitaires & couverture

Ce projet dispose de tests automatisés pour valider les principales fonctionnalités :

### 📂 Fichiers de test

| Fichier                   | Description                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `tests/test_handler.py`   | Vérifie le bon fonctionnement de la fonction `predict()` en mode `zero-shot` et `few-shot`.                           |
| `tests/test_interface.py` | Teste l'interface Gradio, les comportements inattendus (entrée vide, modèle invalide), et la création de l'interface. |

---

### 🧪 Lancer les tests

```bash
python -m pytest --cov=app --cov-report=term-missing
```

Ce qui génère un rapport de couverture avec les lignes non couvertes :

```
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
app/handler.py        16      0   100%
app/interface.py       7      2    71%   17-18
------------------------------------------------
TOTAL                 23      2    91%
```

> 🌟 Les lignes 17-18 non couvertes correspondent à l’exécution directe de l’interface dans le fichier `main.py`.
> Ces lignes ne sont volontairement **pas testées** car elles concernent le lancement interactif de l'application (`iface.launch()`), hors du périmètre des tests unitaires.

---

### 🚫 Hook `pre-push` automatique

Pour garantir la stabilité du dépôt, un **hook Git `pre-push`** a été mis en place.

🧹 Il exécute automatiquement les tests avant chaque `git push`.

#### Exemple `.git/hooks/pre-push`

```bash
#!/bin/sh
echo "🔍 Exécution des tests unitaires avant le push..."
python -m pytest --cov=app --cov-report=term-missing
if [ $? -ne 0 ]; then
  echo "❌ Push bloqué : les tests ont échoué."
  exit 1
fi
```

#### 🔧 Installation manuelle

1. Crée un fichier `.git/hooks/pre-push` si ce n’est pas déjà fait,
2. Colle le script ci-dessus,
3. Rends-le exécutable :

```bash
chmod +x .git/hooks/pre-push
```
