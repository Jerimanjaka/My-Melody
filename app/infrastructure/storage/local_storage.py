import os
from typing import Optional

class LocalStorage:
    def __init__(self, base_path: str):
        self.base_path = os.path.abspath(base_path)
        os.makedirs(self.base_path, exist_ok=True)

    def save(self, filename: str, data: bytes) -> str:
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, 'wb') as f:
            f.write(data)
        return file_path

    def load(self, filename: str) -> Optional[bytes]:
        file_path = os.path.join(self.base_path, filename)
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'rb') as f:
            return f.read()

    def delete(self, filename: str) -> bool:
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def list_files(self) -> list:
        return [
            f for f in os.listdir(self.base_path)
            if os.path.isfile(os.path.join(self.base_path, f))
        ]