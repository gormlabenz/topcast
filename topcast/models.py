from pydantic import BaseModel, Field
from typing import List, Union, Any

class AudioLayer(BaseModel):
    audio: Union[str, bytes, dict]  # Adjust this type if necessary
    is_main: bool = False
    padding_start: float = Field(0, ge=0)
    padding_end: float = Field(0, ge=0)
    volume: float = Field(1, ge=0, le=1)

class Step(BaseModel):
    audio_layers: List[AudioLayer]
    fade_in: float = Field(0, ge=0)
    fade_out: float = Field(0, ge=0)
    overlapping: float = Field(0, ge=0)

class Timeline(BaseModel):
    timeline: List[Step]
