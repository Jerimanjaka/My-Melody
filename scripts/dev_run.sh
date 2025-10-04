#!/bin/bash

# Script de lancement du serveur de développement pour voici-ai

# Activer le mode strict
set -euo pipefail

# Chemin vers le dossier racine du projet
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Activer l'environnement virtuel Python si présent
if [ -d "$PROJECT_ROOT/venv" ]; then
    source "$PROJECT_ROOT/venv/bin/activate"
fi

# Lancer le serveur de développement (adapter la commande selon votre stack)
cd "$PROJECT_ROOT"
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000

# Fin du script