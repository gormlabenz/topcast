from .openai_classes import OpenAIApiBase
import os
from pydub import AudioSegment
from io import BytesIO
import asyncio
from .tts.factory import get_tts_provider

sound_folder = "sounds/"

class PodcastChunk:
    def __init__(self, config):
        self.openai_api_base = OpenAIApiBase(config["system_prompt"], config["messages"], config["get_message"], config["extract"])

    async def generate_podcast_chunk(self, input_text: str, output_file="output.wav", tts_provider="gcp"):
        textItems = await self.openai_api_base.create_chat_completion(input_text)
        
        ttsProvider = get_tts_provider(tts_provider)
        
        # Initialize an empty AudioSegment
        combined_audio = AudioSegment.empty()

        # Run text_to_speech function concurrently for all textItems
        tasks = [asyncio.create_task(ttsProvider.tts(text = textItem['text'], gender = textItem['gender'])) for textItem in textItems]
        
        speech_results = await asyncio.gather(*tasks)

        for speech in speech_results:
            # Convert the audio_content (bytes) to an AudioSegment
            audio_segment = AudioSegment.from_file(BytesIO(speech))
            
            # Concatenate the current audio segment with the combined_audio
            combined_audio += audio_segment

        # Save the combined_audio to the output file
        combined_audio.export(os.path.join(os.getcwd(), sound_folder, output_file), format="wav")

        return output_file
