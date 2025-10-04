from abc import ABC, abstractmethod
from typing import Any

class AudioProcessorPort(ABC):
    @abstractmethod
    def process_audio(self, audio_data: Any) -> Any:
        """
        Process the given audio data and return the result.

        :param audio_data: The input audio data to process.
        :return: The processed audio data.
        """
        pass