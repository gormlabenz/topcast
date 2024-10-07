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
            'male': "George",
            'female': "Laura"
        }
        self.client = AsyncElevenLabs()

    async def tts(self, tts_text: TTSItem):
        voice = self.get_voice(tts_text.gender)

        async def _synthesize_speech():
            audio_generator = await self.client.generate(text=tts_text.text, voice=voice)
            audio_chunks = [chunk async for chunk in audio_generator]
            audio = b''.join(audio_chunks)
            return AudioSegment.from_file(BytesIO(audio))

        return await _synthesize_speech()
