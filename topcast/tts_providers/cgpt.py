import asyncio
from io import BytesIO

from openai import OpenAI
from pydub import AudioSegment

from ..tts_item import TTSItem
from .base import TTSProviderBase


class CGPT(TTSProviderBase):
    def __init__(self):
        super().__init__()
        self.voices = {
            'male': "onyx",
            'female': "nova"
        }
        self.client = OpenAI()

    async def tts(self, tts_text: TTSItem):
        voice = self.get_voice(tts_text.gender)

        async def _synthesize_speech():
            response = await asyncio.to_thread(
                self.client.audio.speech.create,
                model="tts-1",
                voice=voice,
                input=tts_text.text
            )
            audio_content = response.content
            return AudioSegment.from_file(BytesIO(audio_content), format="mp3")

        return await _synthesize_speech()
