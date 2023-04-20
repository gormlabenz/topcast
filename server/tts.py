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

    # Iterate through the list of strings, convert each to speech, and save the result to the output file
    with open(f"sound/{ttsItem['file_name']}", "wb") as f:
        input_text = texttospeech.SynthesisInput(text=ttsItem["text"])
        response = client.synthesize_speech(
            input=input_text, voice=ttsItem["voice"], audio_config=audio_config
        )
        f.write(response.audio_content)


if __name__ == "__main__":
  text_to_speech("This is the first string.")
