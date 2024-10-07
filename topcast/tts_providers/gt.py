import asyncio
from io import BytesIO

from gtts import gTTS
from pydub import AudioSegment

from ..tts_item import TTSItem
from .base import TTSProviderBase


class GTTS(TTSProviderBase):
    def __init__(self):
        super().__init__()

    async def tts(self, tts_text: TTSItem):
        return await asyncio.to_thread(self._synthesize_speech, tts_text)

    def _synthesize_speech(self, tts_text: TTSItem):
        mp3_fp = BytesIO()
        tts = gTTS(text=tts_text.text, lang='en')
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        return AudioSegment.from_file(mp3_fp, format="mp3")
