import asyncio
from io import BytesIO

from elevenlabs.client import AsyncElevenLabs
from pydub import AudioSegment

from ..tts_item import TTSItem
from .base import TTSProviderBase


class ElevenLabs(TTSProviderBase):
    def __init__(self):
        super().__init__()
        self.voices = {
            'male': "Adam",
            'female': "Bella"
        }
        self.client = AsyncElevenLabs()  # Initialize the async client

    async def tts(self, tts_text: TTSItem):
        voice = self.get_voice(tts_text.gender)

        async def _synthesize_speech():
            audio = await self.client.generate(text=tts_text.text, voice=voice)
            return AudioSegment.from_file(BytesIO(audio))

        return await _synthesize_speech()
