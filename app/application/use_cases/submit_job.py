from typing import Any, Dict
from app.domain.models import Job
from app.domain.repositories import JobRepository

class SubmitJobUseCase:
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    def execute(self, job_data: Dict[str, Any]) -> Job:
        job = Job(**job_data)
        saved_job = self.job_repository.save(job)
        return saved_job