from .base import TTSProviderBase
from ..models import TTSItem

import asyncio
from elevenlabs import generate
from pydub import AudioSegment
from io import BytesIO

class ElevenLabs(TTSProviderBase):
    def __init__(self):
        super().__init__()
        self.voices = {
            'male': "Adam",
            'female': "Bella"
        }

    async def tts(self, tts_text: TTSItem):
        voice = self.get_voice(tts_text.gender)
        
        def _synthesize_speech():
          return  AudioSegment.from_file(BytesIO(generate(text=tts_text.text, voice=voice)))
    
    # Run the synchronous Text-to-Speech code in a separate thread
        return await asyncio.to_thread(_synthesize_speech)
