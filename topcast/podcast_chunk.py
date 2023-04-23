from .chatgpt import ChatGPT
import time
from pydub import AudioSegment
from io import BytesIO
import asyncio
from .tts.factory import get_tts_provider



class PodcastChunk:
    def __init__(self, config):
        self.chatgpt = ChatGPT(config["system_prompt"], config["messages"], config["get_message"], config["extract"])

    async def generate_podcast_chunk(self, input_text: str, tts_provider="gcp"):
        textItems = await self.chatgpt.create_chat_completion(input_text)
        
        ttsProvider = get_tts_provider(tts_provider)
        
        print(textItems)
        
        # Initialize an empty AudioSegment
        combined_audio = AudioSegment.empty()

        # Run text_to_speech function concurrently for all textItems
        tasks = [asyncio.create_task(ttsProvider.tts(text = textItem['text'], gender = textItem['gender'])) for textItem in textItems]
        
        speech_results = await run_tasks(tasks, run_async = True if tts_provider == "gcp" else False)

        for speech in speech_results:
            # Convert the audio_content (bytes) to an AudioSegment
            audio_segment = AudioSegment.from_file(BytesIO(speech))
            
            # Concatenate the current audio segment with the combined_audio
            combined_audio += audio_segment

        return combined_audio


async def run_tasks(tasks, run_async = False):
    if run_async:
        # Run tasks asynchronously using asyncio.gather
        results = await asyncio.gather(*tasks)
    else:
        # Run tasks synchronously in a loop
        results = []
        for task in tasks:
            result = await task
            results.append(result)
            
    return results
