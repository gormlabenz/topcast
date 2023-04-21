from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from .podcast_chunk import PodcastChunk
from .configs import summary_config, interview_config, conclusion_config

class Item(BaseModel):
    text: str
    tts_provider: Optional[str] = "gcp"
    
app = FastAPI()

@app.post("/generate_podcast/")
async def generate_podcast_text(item: Item):
    podcastChunk = PodcastChunk(summary_config)
    result = await podcastChunk.generate_podcast_chunk(input_text=item.text, tts_provider=item.tts_provider)
    
    return {"result": result}
