import openai
from fastapi import HTTPException

from .models import AudioContent

class ChatGPT:
    def __init__(self, audio_content: AudioContent):
        self.theme = audio_content.theme()

    async def create_chat_completion(self, input_message: str):
        try:
            messages = self.theme.get_messages(input_message=input_message)
            
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            content = completion.choices[0].message.content
            
            return self.theme.extract_content(content)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
          


