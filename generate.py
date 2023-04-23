from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs, GCP
import os
from topcast import generate, set_elevenlab_api_key, set_google_credentials, set_openai_api_key

set_elevenlab_api_key(os.environ["ELEVENLAB_API_KEY"])
set_openai_api_key(os.environ["OPENAI_API_KEY"])
set_google_credentials('gcp-keyfile.json')

timeline = [
    {
        "audio_layers": [
            {
                "audio": 'sounds/jingle.wav', # audio as a byte array,
                "is_main": True, # if True, this audio sets the length of the step in the timeline
                "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                "volume": 1 # volume of the audio, 1 is normal, 0 is muted
            }
        ],
    },
    {
    "audio_layers": [
        {
            "audio": {
                "content": "Der Siamesische Kampffisch ist ein in Thailand und Kambodscha beheimateter Labyrinthfisch. Das erste Auftauchen dieser Fischart wird auf 1892 in Japan datiert. Sie wurde aber bereits viele Jahre zuvor von Einheimischen, vor allem wegen der Aggressivität der Männchen untereinander, für Schau- und Wettkämpfe gezüchtet.",
                "theme": Introduction,
                "tts_provider": ElevenLabs
            }, # audio as a byte array,
            "is_main": True, # if True, this audio sets the length of the step in the timeline
            "padding_start": 1600, # milliseconds, how much time to add before the audio gets played
            "padding_end": 1200, # milliseconds, how much time to add after the audio gets played
            "volume": 1 # volume of the audio, 1 is normal, 0 is muted
        }
    ],
    "fade-in": 0, # milliseconds, how much time to fade in the audio
    "crossfade": 2400, # milliseconds, how much time to overlap the audio with the step before
    "fade-out": 1800,
},
]

podcast = generate(timeline)
podcast.export("podcast_2.wav", format="wav")

