from .base import TTSProviderBase
from google.cloud import texttospeech
import asyncio
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-keyfile.json"

class GCPProvider(TTSProviderBase):
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
        
    async def tts(self, text: str, gender: str):
        voice = self.get_voice(gender)
        
        def _synthesize_speech():
          client = texttospeech.TextToSpeechClient()

          # Set the audio configuration
          audio_config = texttospeech.AudioConfig(
              audio_encoding=texttospeech.AudioEncoding.LINEAR16
          )
          

          input_text = texttospeech.SynthesisInput(text=text)
          return client.synthesize_speech(
                  input=input_text, voice=voice, audio_config=audio_config
              ).audio_content
    
    # Run the synchronous Text-to-Speech code in a separate thread
        return await asyncio.to_thread(_synthesize_speech)
