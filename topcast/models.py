from pydantic import BaseModel, Field, validator
from typing import List, Union, Any, Type
from topcast.chatgpt_themes.base import ChatGPTThemeBase
from topcast.tts_providers.base import TTSProviderBase

class AudioContent(BaseModel):
    content: str
    theme: Type[ChatGPTThemeBase]
    tts_provider: Type[TTSProviderBase]

    @validator("theme")
    def check_theme_base_class(cls, value):
        if not issubclass(value, ChatGPTThemeBase):
            raise ValueError("The provided theme class does not inherit from ChatGPTThemeBase.")
        return value

    @validator("tts_provider")
    def check_tts_provider_base_class(cls, value):
        if not issubclass(value, TTSProviderBase):
            raise ValueError("The provided TTS provider class does not inherit from TTSProviderBase.")
        return value


class AudioLayer(BaseModel):
    audio: Union[str, bytes, AudioContent]
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
