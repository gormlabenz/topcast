import openai
from fastapi import HTTPException
from .prompts import summaryPrompts, interviewPrompts, conclusionPrompts
from typing import Callable
from dotenv import load_dotenv
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")
load_dotenv()

print("openai.api_key", openai.api_key, os.getenv("OPENAI_API_KEY"))

class OpenAIApiBase:
    def __init__(self, system_prompt: str, messages: list, get_message: Callable, extract: Callable):
        self.system_prompt = system_prompt
        self.messages = messages
        self.get_message  = get_message
        self.extract = extract

    async def create_chat_completion(self, input_message: str):
        try:
            messages = self.get_messages(input_message)
            print("create")
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            print("response" , completion.choices[0].message)

            return self.extract(completion.choices[0].message.content)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
          
    def get_messages(self, input_message:str):
        messages = self.messages.copy()
        messages.append({
          "role":"user", "content":self.get_message(input_message)})
        
        return messages

OpenAIApiCreateSummary = OpenAIApiBase(system_prompt=summaryPrompts["system_prompt"], messages=summaryPrompts["messages"], get_message=summaryPrompts["get_message"], extract=summaryPrompts["extract"])

OpenAIApiInterview = OpenAIApiBase(system_prompt=interviewPrompts["system_prompt"], messages=interviewPrompts["messages"], get_message=interviewPrompts["get_message"], extract=interviewPrompts["extract"])

OpenAIApiConclusion = OpenAIApiBase(system_prompt=conclusionPrompts["system_prompt"], messages=conclusionPrompts["messages"], get_message=conclusionPrompts["get_message"], extract=conclusionPrompts["extract"])
