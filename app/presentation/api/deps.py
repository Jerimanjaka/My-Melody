from fastapi import Depends
from app.presentation.api.dependencies import get_db, get_current_user

# Exemple de dépendances à utiliser dans vos endpoints FastAPI

def common_parameters(q: str = None, limit: int = 10, offset: int = 0):
    return {"q": q, "limit": limit, "offset": offset}

def get_active_user(current_user=Depends(get_current_user)):
    if not current_user.is_active:
        raise Exception("Inactive user")
    return current_user

# Ajoutez ici d'autres dépendances personnalisées selon vos besoins