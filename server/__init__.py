from fastapi import FastAPI
from pydantic import BaseModel

from .podcast_chunk import PodcastChunk
from .configs import summary_config, interview_config, conclusion_config

class Item(BaseModel):
    text: str
    
    
app = FastAPI()

@app.post("/generate_podcast/")
async def generate_podcast_text(item: Item):
    podcastChunk = PodcastChunk(interview_config)
    result = await podcastChunk.generate_podcast(input_text=item.text)
    
    return {"result": result}
