class DomainException(Exception):
    """Exception de base pour le domaine de l'application."""
    pass


class EntityNotFoundException(DomainException):
    """Exception levée lorsqu'une entité n'est pas trouvée."""
    pass


class ValidationException(DomainException):
    """Exception levée lors d'une erreur de validation."""
    pass