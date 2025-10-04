from typing import Any, Dict

class InferenceService:
    def __init__(self, model: Any):
        self.model = model

    def predict(self, input_data: Dict) -> Any:
        """
        Effectue une prédiction à partir des données d'entrée.

        Args:
            input_data (Dict): Les données d'entrée pour le modèle.

        Returns:
            Any: Le résultat de la prédiction.
        """
        # Exemple d'utilisation du modèle, à adapter selon votre cas
        return self.model.predict(input_data)