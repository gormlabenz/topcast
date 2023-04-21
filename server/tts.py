import os
from google.cloud import texttospeech
from .models import TTSItem

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-keyfile.json"


def text_to_speech(ttsItem: TTSItem):
    client = texttospeech.TextToSpeechClient()

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    input_text = texttospeech.SynthesisInput(text=ttsItem["text"])
    return client.synthesize_speech(
            input=input_text, voice=ttsItem["voice"], audio_config=audio_config
        )

