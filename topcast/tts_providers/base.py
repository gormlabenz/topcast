from abc import ABC, abstractmethod
from topcast.models import TTSText

class TTSProviderBase(ABC):
    def __init__(self):
        self.voices = {}

    def get_voice(self, gender):
        return self.voices.get(gender.lower())
    
    @abstractmethod
    def tts(self, tts_text: TTSText):
        pass
