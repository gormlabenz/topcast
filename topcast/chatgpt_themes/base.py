from abc import ABC, abstractmethod

from openai import OpenAI

client = OpenAI()


class ChatGPTThemeBase(ABC):
    def __init__(self):
        self.system_prompt = ""
        self.messages = []

    def get_messages(self, input_message: str):
        messages = self.messages.copy()
        # insert system prompt at the beginning
        messages.insert(0, {
            "role": "system", "content": self.system_prompt})

        messages.append({
            "role": "user", "content": self.create_content(input_message)})

        return messages

    async def create_chat_completion(self, input_message: str):
        messages = self.get_messages(input_message=input_message)

        completion = client.chat.completions.create(model="gpt-4o",
                                                    messages=messages)
        content = completion.choices[0].message.content

        return self.extract_content(content)

    @abstractmethod
    def create_content(self, input_content: str):
        pass

    @abstractmethod
    def extract_content(self, response_content: str):
        pass
