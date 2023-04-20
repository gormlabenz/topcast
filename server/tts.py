import os
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-keyfile.json"


def text_to_speech(text, output_file="output.mp3"):
    client = texttospeech.TextToSpeechClient()

    # Set the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Iterate through the list of strings, convert each to speech, and save the result to the output file
    with open(output_file, "wb") as f:
        input_text = texttospeech.SynthesisInput(text=text)
        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )
        f.write(response.audio_content)


if __name__ == "__main__":
  text_to_speech("This is the first string.")
