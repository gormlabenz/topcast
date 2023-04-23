import openai
from fastapi import HTTPException

from typing import Callable
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self, system_prompt: str, messages: list, get_message: Callable, extract: Callable):
        self.system_prompt = system_prompt
        self.messages = messages
        self.get_message  = get_message
        self.extract = extract

    async def create_chat_completion(self, input_message: str):
        try:
            messages = self.get_messages(input_message)
            print("fetching")
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            print("fetched", completion.choices[0].message.content)

            return self.extract(completion.choices[0].message.content)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
          
    def get_messages(self, input_message:str):
        messages = self.messages.copy()
        messages.append({
          "role":"user", "content":self.get_message(input_message)})
        
        return messages
