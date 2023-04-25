from .base import ChatGPTThemeBase
from topcast.models import TTSItem

class NoneTheme(ChatGPTThemeBase):
    def __init__(self):
        pass
        
    def get_messages(self, input_message:str):
        pass
    
    async def create_chat_completion(self, input_message: str):
            return [TTSItem(text=input_message, gender="male")]
              
        
    def create_content(self, input_content: str):
        pass
      
    def extract_content(self, response_content: str):
        pass
