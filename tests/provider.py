import asyncio
from io import BytesIO
from pydub import AudioSegment
from server.tts.elevenlabs_provider import ElevenLabsProvider

async def main():
    text = "Hello, this is a test text for debugging purposes."
    gender = "male"

    tts_provider = ElevenLabsProvider()
    speech_result = await tts_provider.tts(text, gender)

    # Saving the speech_result to a file
    with open("output.mp3", "wb") as f:
        f.write(speech_result)

    # Load the saved file and play it
    audio_segment = AudioSegment.from_file("output.mp3", format="mp3")
    audio_segment.export("output_2.wav", format="wav")

if __name__ == "__main__":
    asyncio.run(main())
