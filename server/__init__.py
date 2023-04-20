from fastapi import FastAPI
from pydantic import BaseModel

from .podcaster import Podcaster
from .configs import summaryConfig, interviewConfig, conclusionConfig

class Item(BaseModel):
    text: str
    
    
app = FastAPI()

@app.post("/generate_podcast/")
async def generate_podcast_text(item: Item):
    podcaster = Podcaster(interviewConfig)
    result = await podcaster.generate_podcast(input_text=item.text)
    
    return {"result": result}
