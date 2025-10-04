from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class AudioId:
    value: str

    @staticmethod
    def generate() -> 'AudioId':
        return AudioId(str(uuid.uuid4()))

    def __post_init__(self):
        if not self.value or not isinstance(self.value, str):
            raise ValueError("AudioId value must be a non-empty string.")