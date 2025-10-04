from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

class Job(BaseModel):
    id: int
    title: str
    description: str

# Dummy in-memory storage
jobs_db = [
    Job(id=1, title="Développeur Python", description="Développement d'applications backend."),
    Job(id=2, title="Data Scientist", description="Analyse de données et modélisation."),
]

@router.get("/", response_model=List[Job])
def list_jobs():
    return jobs_db

@router.get("/{job_id}", response_model=Job)
def get_job(job_id: int):
    for job in jobs_db:
        if job.id == job_id:
            return job
    raise HTTPException(status_code=404, detail="Job not found")

@router.post("/", response_model=Job)
def create_job(job: Job):
    jobs_db.append(job)
    return job