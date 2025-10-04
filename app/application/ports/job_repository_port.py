from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.job import Job

class JobRepositoryPort(ABC):
    @abstractmethod
    def get_by_id(self, job_id: int) -> Optional[Job]:
        pass

    @abstractmethod
    def list(self) -> List[Job]:
        pass

    @abstractmethod
    def create(self, job: Job) -> Job:
        pass

    @abstractmethod
    def update(self, job: Job) -> Job:
        pass

    @abstractmethod
    def delete(self, job_id: int) -> None:
        pass