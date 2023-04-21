import os
from google.cloud import texttospeech
from .models import TTSItem
import asyncio

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-keyfile.json"

async def text_to_speech(ttsItem: TTSItem):
    def _synthesize_speech():
        client = texttospeech.TextToSpeechClient()

        # Set the audio configuration
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )
        
        print(ttsItem)

        input_text = texttospeech.SynthesisInput(text=ttsItem["text"])
        return client.synthesize_speech(
                input=input_text, voice=ttsItem["voice"], audio_config=audio_config
            )
    
    # Run the synchronous Text-to-Speech code in a separate thread
    return await asyncio.to_thread(_synthesize_speech)
