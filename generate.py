from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs, GCP
from topcast import generate

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

t = [
        {
            "audio_layers": [
                {
                    "audio": 'sounds/summary.wav', # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                }
            ],
        }
    ]




podcast = generate(t)
podcast.export("podcast_3.wav", format="wav")

