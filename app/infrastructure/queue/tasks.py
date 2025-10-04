from celery import shared_task

@shared_task
def example_task(data):
    """
    Exemple de tâche Celery.
    Traite les données reçues.
    """
    # Traitement fictif
    result = f"Traitement des données : {data}"
    return result