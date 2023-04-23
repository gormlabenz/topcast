from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs, GCP
from topcast.models import Timeline
from pydub import AudioSegment
from topcast.podcaster import Podcaster
import pprint

timeline = [
    {
        "audio_layers": [
            {
                "audio": {
                    "content": "Data validation and settings management using Python type annotations. pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid. Define how data should be in pure, canonical Python; validate it with pydantic",
                    "theme": Introduction,
                    "tts_provider": GCP
                    },
                "is_main": True,
                "padding_start": 1600,
                "padding_end": 1200,
                "volume": 1
            },
        ],
        "fade_in": 0,
        "overlapping": 2400,
        "fade_out": 1800,
    },
]

try:
    validated_timeline = Timeline(timeline=timeline)
    t = Podcaster(timeline).generate()
    pprint.pprint(t)
except ValueError as e:
    print(f"Timeline validation error: {e}")
