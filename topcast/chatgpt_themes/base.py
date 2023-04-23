from abc import ABC, abstractmethod

class ChatGPTThemeBase(ABC):
    def __init__(self):
        self.system_prompt = ""
        self.messages = []
    
    def get_messages(self, input_content: str):
        messages = self.messages.copy()
        return messages.append({"role": "user", "content": self.create_content(input_content)})
    
    @abstractmethod
    def create_content(self, input_content: str):
        pass
      
    @abstractmethod
    def extract_content(self, response_content: str):
        pass
