class DummyProcessor:
    """
    Un processeur factice pour simuler le traitement AI.
    """

    def __init__(self):
        pass

    def process(self, data):
        """
        Traite les données en les retournant telles quelles.

        Args:
            data (any): Les données à traiter.

        Returns:
            any: Les données traitées (inchangées).
        """
        return data