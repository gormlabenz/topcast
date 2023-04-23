from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs, GCP
from topcast.podcaster import Podcaster

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
        "fade_in": 1,
        "crossfade": 2400,
        "fade_out": 1800,
    },
]


podcast = Podcaster(timeline)
podcast.generate()
podcast.save()

