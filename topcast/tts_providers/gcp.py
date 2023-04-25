from .base import TTSProviderBase
from google.cloud import texttospeech
import asyncio
from topcast.models import TTSItem
from pydub import AudioSegment
from io import BytesIO

class GCP(TTSProviderBase):
    def __init__(self):
        super().__init__()
        self.voices = {
            'male': texttospeech.VoiceSelectionParams(
                language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE,
                name="en-US-Neural2-J"
            ),
            'female': texttospeech.VoiceSelectionParams(
                language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
                name="en-US-Neural2-C"
            )
        }
        
    async def tts(self, tts_text: TTSItem):
        voice = self.get_voice(tts_text.gender)
        
        def _synthesize_speech():
          client = texttospeech.TextToSpeechClient()

          # Set the audio configuration
          audio_config = texttospeech.AudioConfig(
              audio_encoding=texttospeech.AudioEncoding.LINEAR16
          )
          

          input_text = texttospeech.SynthesisInput(text=tts_text.text)
          return AudioSegment.from_file(BytesIO(client.synthesize_speech(
                  input=input_text, voice=voice, audio_config=audio_config
              ).audio_content))
    
    # Run the synchronous Text-to-Speech code in a separate thread
        return await asyncio.to_thread(_synthesize_speech)
