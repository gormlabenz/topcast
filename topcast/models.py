from typing import Any, List, Optional, Type, Union

from pydantic import BaseModel, ConfigDict, Field, validator
from pydub.audio_segment import AudioSegment

from topcast.chatgpt_themes.base import ChatGPTThemeBase
from topcast.chatgpt_themes.none_theme import NoneTheme
from topcast.tts_item import TTSItem
from topcast.tts_providers.base import TTSProviderBase
from topcast.tts_providers.cgpt import CGPT
from topcast.tts_providers.gt import GTTS


class ChapterData(BaseModel):
    raw_audio: Optional[AudioSegment] = None
    text_list: List[TTSItem] = Field(default_factory=list)
    audio_list: List[AudioSegment] = Field(default_factory=list)

    model_config = ConfigDict(arbitrary_types_allowed=True)


class AudioItem(BaseModel):

    content: str
    theme: Optional[Type[ChatGPTThemeBase]] = Field(default=NoneTheme)
    tts_provider: Optional[Type[TTSProviderBase]] = Field(default=GTTS)

    @validator("theme")
    def check_theme_base_class(cls, value):
        from topcast.chatgpt_themes.base import ChatGPTThemeBase

        if not issubclass(value, ChatGPTThemeBase):
            raise ValueError(
                "The provided theme class does not inherit from ChatGPTThemeBase.")
        return value

    @validator("tts_provider")
    def check_tts_provider_base_class(cls, value):
        from topcast.tts_providers.base import TTSProviderBase

        if not issubclass(value, TTSProviderBase):
            raise ValueError(
                "The provided TTS provider class does not inherit from TTSProviderBase.")
        return value


class AudioLayer(BaseModel):
    audio: Union[str, AudioSegment, AudioItem]
    data: ChapterData = None
    sets_length: bool = False
    fade_in: int = Field(1, ge=1)
    fade_out: int = Field(1, ge=1)
    padding_start: int = Field(0, ge=0)
    padding_end: int = Field(0, ge=0)
    crossfade: int = Field(0, ge=0)
    volume: int = Field(1, ge=0, le=1)

    class Config:
        arbitrary_types_allowed = True


class Chapter(BaseModel):
    audio_layers: List[AudioLayer]
    fade_in: int = Field(1, ge=1)
    fade_out: int = Field(1, ge=1)
    padding_start: int = Field(0, ge=0)
    padding_end: int = Field(0, ge=0)
    crossfade: int = Field(0, ge=0)
    volume: float = Field(1, ge=0, le=1)


class Timeline(BaseModel):
    timeline: List[Chapter]
