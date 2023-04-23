from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs
from topcast.models import Timeline
from pydub import AudioSegment
from topcast.podcaster import Podcaster

timeline = [
    {
        "audio_layers": [
            {
                "audio": "podcast.wav",
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
    print("Timeline is valid!", t)
except ValueError as e:
    print(f"Timeline validation error: {e}")
