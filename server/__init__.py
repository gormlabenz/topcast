from fastapi import FastAPI
from pydantic import BaseModel


from .openai_classes import OpenAIApiInterview

class Item(BaseModel):
    text: str
    
    
app = FastAPI()

@app.post("/generate_podcast/")
async def generate_podcast_text(item: Item):
  
    result = await OpenAIApiInterview.create_chat_completion(input_message=item.text)
    
    return {"result": result}
