from typing import Optional
from app.domain.repositories.job_repository import JobRepository
from app.domain.entities.job import JobStatus

class GetJobStatusUseCase:
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    def execute(self, job_id: str) -> Optional[JobStatus]:
        job = self.job_repository.get_by_id(job_id)
        if job is None:
            return None
        return job.status