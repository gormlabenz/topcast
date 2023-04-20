from .openai_classes import OpenAIApiBase
from .tts import text_to_speech

class Podcaster:
    def __init__(self, config):
        self.openai_api_base = OpenAIApiBase(config["system_prompt"], config["messages"], config["get_message"], config["extract"])

    async def generate_podcast(self, input_text: str, output_file="output.mp3"):
        textItems = await self.openai_api_base.create_chat_completion(input_text)
        
        for textItem in textItems:
          text_to_speech(textItem)
        
        return output_file
