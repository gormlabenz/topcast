from pydantic import BaseModel
from typing import Optional

class InputData(BaseModel):
    system_prompt: str
    conversation: list
    tts_provider: Optional[str] = "gcp"
