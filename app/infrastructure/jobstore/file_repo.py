import os
import json
from typing import Any, Dict, Optional

class FileJobRepository:
    def __init__(self, directory: str):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def _get_job_path(self, job_id: str) -> str:
        return os.path.join(self.directory, f"{job_id}.json")

    def save_job(self, job_id: str, job_data: Dict[str, Any]) -> None:
        path = self._get_job_path(job_id)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(job_data, f, ensure_ascii=False, indent=2)

    def load_job(self, job_id: str) -> Optional[Dict[str, Any]]:
        path = self._get_job_path(job_id)
        if not os.path.exists(path):
            return None
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def delete_job(self, job_id: str) -> None:
        path = self._get_job_path(job_id)
        if os.path.exists(path):
            os.remove(path)

    def list_jobs(self) -> Dict[str, Dict[str, Any]]:
        jobs = {}
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                job_id = filename[:-5]
                jobs[job_id] = self.load_job(job_id)
        return jobs