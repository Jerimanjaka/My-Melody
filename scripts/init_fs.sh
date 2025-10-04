#!/bin/bash

# Initialisation du système de fichiers pour voici-ai

set -e

# Définir les dossiers à créer
DIRS=(
    "data"
    "logs"
    "models"
    "output"
    "tmp"
)

echo "Initialisation des dossiers du projet..."

for dir in "${DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "Créé: $dir"
    else
        echo "Déjà présent: $dir"
    fi
done

echo "Initialisation terminée."