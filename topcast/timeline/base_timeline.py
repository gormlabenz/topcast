from abc import ABC, abstractmethod

class Timeline(ABC):
    @abstractmethod
    def get_timeline(audio_list):
        pass
