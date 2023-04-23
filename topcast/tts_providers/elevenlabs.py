from .base import TTSProviderBase
import asyncio
import os
from elevenlabs import set_api_key, generate
from dotenv import load_dotenv
from topcast.models import TTSText
from pydub import AudioSegment
from io import BytesIO

load_dotenv()

set_api_key(os.getenv("ELEVENLAB_API_KEY"))

class ElevenLabs(TTSProviderBase):
    def __init__(self):
        super().__init__()
        self.voices = {
            'male': "Adam",
            'female': "Bella"
        }

    async def tts(self, tts_text: TTSText):
        voice = self.get_voice(tts_text.gender)
        
        def _synthesize_speech():
          return  AudioSegment.from_file(BytesIO(generate(text=tts_text.text, voice=voice)))
    
    # Run the synchronous Text-to-Speech code in a separate thread
        return await asyncio.to_thread(_synthesize_speech)
