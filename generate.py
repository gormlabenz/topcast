from topcast.chatgpt_themes import introduction, interview, conclusion, summary
from topcast.tts_providers import elevenlabs
from topcast.models import Timeline
from pydub import AudioSegment

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
print(type(AudioSegment.from_file("podcast.wav")))
try:
    validated_timeline = Timeline(timeline=timeline)
    print("Timeline is valid!")
except ValueError as e:
    print(f"Timeline validation error: {e}")
