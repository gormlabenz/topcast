from abc import ABC, abstractmethod

class TTSProviderBase(ABC):
    def __init__(self):
        self.voices = {}

    def get_voice(self, gender):
        return self.voices.get(gender.lower())
    
    @abstractmethod
    def tts(self, text, gender):
        pass
