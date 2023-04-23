from pydantic import BaseModel, Field, validator
from typing import List, Union, Any, Type
from pydub.audio_segment import AudioSegment


class TTSText(BaseModel):
    text: str
    gender: str

class StepData(BaseModel):
    raw_audio: AudioSegment = None
    text_list: List[TTSText] = []
    audio_list: List[AudioSegment] = []

    class Config:
        arbitrary_types_allowed = True
        
class AudioContent(BaseModel):
    from topcast.tts_providers.base import TTSProviderBase
    from topcast.chatgpt_themes.base import ChatGPTThemeBase
    
    content: str
    theme: Type[ChatGPTThemeBase]
    tts_provider: Type[TTSProviderBase]

    @validator("theme")
    def check_theme_base_class(cls, value):
        from topcast.chatgpt_themes.base import ChatGPTThemeBase
        
        if not issubclass(value, ChatGPTThemeBase):
            raise ValueError("The provided theme class does not inherit from ChatGPTThemeBase.")
        return value

    @validator("tts_provider")
    def check_tts_provider_base_class(cls, value):
        from topcast.tts_providers.base import TTSProviderBase
        
        if not issubclass(value, TTSProviderBase):
            raise ValueError("The provided TTS provider class does not inherit from TTSProviderBase.")
        return value

class AudioLayer(BaseModel):
    audio: Union[str, AudioSegment, AudioContent]
    data: StepData = None
    is_main: bool = False
    fade_in: int = Field(1, ge=1)
    fade_out: int = Field(1, ge=1)
    padding_start: int = Field(0, ge=0)
    padding_end: int = Field(0, ge=0)
    crossfade: int = Field(0, ge=0)
    volume: int = Field(1, ge=0, le=1)
    
    class Config:
        arbitrary_types_allowed = True
        
class Step(BaseModel):
    audio_layers: List[AudioLayer]
    fade_in: int = Field(1, ge=1)
    fade_out: int = Field(1, ge=1)
    padding_start: int = Field(0, ge=0)
    padding_end: int = Field(0, ge=0)
    crossfade: int = Field(0, ge=0)
    volume: float = Field(1, ge=0, le=1)
    

class Timeline(BaseModel):
    timeline: List[Step]
