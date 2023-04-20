from .openai_classes import OpenAIApiBase
from .tts import text_to_speech

class Podcaster:
    def __init__(self, config):
        self.openai_api_base = OpenAIApiBase(config["system_prompt"], config["messages"], config["get_message"], config["extract"])

    async def generate_podcast(self, input_text: str, output_file="output.mp3"):
        texts = await self.openai_api_base.create_chat_completion(input_text)
        
        for text in texts:
          # filename consiting of the first 10 characters of the text
          filename = text[:10]
          text_to_speech(text, f"sound/{filename}.mp3")
        
        return output_file
