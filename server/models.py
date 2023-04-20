from pydantic import BaseModel
from google.cloud import texttospeech

class InputData(BaseModel):
    system_prompt: str
    conversation: list

class TTSItem(BaseModel):
    text: str
    filename: str
    voice: texttospeech.VoiceSelectionParams
    
    class Config:
        arbitrary_types_allowed = True
