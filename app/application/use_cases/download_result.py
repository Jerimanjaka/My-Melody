from typing import Optional
from app.domain.repositories.result_repository import ResultRepository
from app.domain.entities.result import Result

class DownloadResultUseCase:
    def __init__(self, result_repository: ResultRepository):
        self.result_repository = result_repository

    def execute(self, result_id: str) -> Optional[bytes]:
        result: Optional[Result] = self.result_repository.get_by_id(result_id)
        if result and result.file_path:
            try:
                with open(result.file_path, "rb") as file:
                    return file.read()
            except FileNotFoundError:
                return None
        return None