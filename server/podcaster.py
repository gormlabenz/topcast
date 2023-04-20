from .openai_classes import OpenAIApiBase
from .tts import text_to_speech
import os
from pydub import AudioSegment
from io import BytesIO

sound_folder = "sounds/"

class Podcaster:
    def __init__(self, config):
        self.openai_api_base = OpenAIApiBase(config["system_prompt"], config["messages"], config["get_message"], config["extract"])

    async def generate_podcast(self, input_text: str, output_file="output.wav"):
        textItems = await self.openai_api_base.create_chat_completion(input_text)
        
        # Initialize an empty AudioSegment
        combined_audio = AudioSegment.empty()

        for textItem in textItems:
            print("textItem: ", textItem)
            speech = text_to_speech(textItem)
            
            # Convert the audio_content (bytes) to an AudioSegment
            audio_segment = AudioSegment.from_file(BytesIO(speech.audio_content), format="wav")
            
            # Concatenate the current audio segment with the combined_audio
            combined_audio += audio_segment

        # Save the combined_audio to the output file
        combined_audio.export(os.path.join(os.getcwd(), sound_folder, output_file), format="wav")

        return output_file
