from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import asyncio
from wikipediaapi import Wikipedia
import time 

from .podcast_chunk import PodcastChunk
from .configs import intro_config, interview_config, conclusion_config, summary_config
from .podcast_builder import PodcastBuilder

from .timeline.long_timeline import LongTimeline
from .timeline.short_timeline import ShortTimeline

sound_folder = "sounds/"
output_file="interview.wav"

app = FastAPI()

class Item(BaseModel):
    text: str
    tts_provider: Optional[str] = "gcp"

class SearchTerm(BaseModel):
    term: str
    tts_provider: Optional[str] = "gcp"

@app.post("/wikipedia/")
async def generate_podcast_wikipedia(search_term: SearchTerm):
    wiki = Wikipedia('en')
    page = wiki.page(search_term.term)
    
    if not page.exists():
        return {"error": f"Page not found for the search term '{search_term.term}'"}

    summary = page.summary[0:1000]  # Get the first 1000 characters of the summary
    
    return {"summary": summary}

    item = Item(text=summary, tts_provider=search_term.tts_provider)
    return await generate_podcast_text(item=item)

@app.post("/generate_podcast/")
async def generate_podcast_text(item: Item):
    
    tasks = []
    timeline = None
    
    if len(item.text) > 400:
        intro_chunk = PodcastChunk(intro_config)
        interview_chunk = PodcastChunk(interview_config)
        conclusion_chunk = PodcastChunk(conclusion_config)

        tasks = [
            intro_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="elevenlabs"),
            interview_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="gcp"),
            conclusion_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="elevenlabs")
        ]
        
        timeline = LongTimeline
    else:
        summary_chunk = PodcastChunk(summary_config)
        tasks = [
            summary_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="elevenlabs")
        ]
        timeline = ShortTimeline
        
    
    audio_list = await asyncio.gather(*tasks)
    podcast_builder = PodcastBuilder(timeline.get_timeline(audio_list))
    output_file = podcast_builder.build(output_file='sounds/podcast.wav')
    
    return {"result": output_file}
