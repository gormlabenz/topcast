from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os
import asyncio

from .podcast_chunk import PodcastChunk
from .configs import summary_config, interview_config, conclusion_config
from .podcast_builder import PodcastBuilder

sound_folder = "sounds/"
output_file="interview.wav"

class Item(BaseModel):
    text: str
    tts_provider: Optional[str] = "gcp"
    
app = FastAPI()

@app.post("/generate_podcast/")
async def generate_podcast_text(item: Item):
    summary_chunk = PodcastChunk(summary_config)
    interview_chunk = PodcastChunk(interview_config)
    conclusion_chunk = PodcastChunk(conclusion_config)
    
    tasks = [
        summary_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="elevenlabs"),
        interview_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="gcp"),
        conclusion_chunk.generate_podcast_chunk(input_text=item.text, tts_provider="elevenlabs")
    ]
    
    results = await asyncio.gather(*tasks)
    
    timeline = [
        {
            "audio": [
                {
                    "audio": 'sounds/jingle.wav', # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                }
            ],
        
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "fade-out": 0, # milliseconds, how much time to fade out the audio
        },
            {
            "audio": [
                {
                    "audio": results[0], # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 1600, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 1200, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                },
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
            "fade-out": 1800,
        },
            {
            "audio": [
                {
                    "audio": results[1], # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 1600, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 1800, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                },
                {
                    "audio": 'sounds/background.mp3', # audio as a byte array,
                    "is_main": False, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                    "volume": 0.2 # volume of the audio, 1 is normal, 0 is muted
                }
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
            "fade-out": 1800,
        },
            {
            "audio": [
                {
                    "audio": results[2], # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 2800, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 1800, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                }
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
            "fade-out": 1800,
        }
            
    ]

    podcast_builder = PodcastBuilder(timeline)
    output_file = podcast_builder.build(output_file='sounds/podcast.wav')
    
    return {"result": output_file}
