from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary, NoneTheme
from topcast.tts_providers import ElevenLabs, GCP, GTTS
import os
from topcast import generate, set_elevenlab_api_key, set_google_credentials, set_openai_api_key

from dotenv import load_dotenv

load_dotenv()

set_elevenlab_api_key(os.environ["ELEVENLAB_API_KEY"])
set_openai_api_key(os.environ["OPENAI_API_KEY"])
set_google_credentials('gcp-keyfile.json')

timeline = [
    {
        "audio_layers": [
            {
                "audio": 'sounds/jingle.wav', 
                "sets_length": True, 
            }
        ],
    },
        {
    "audio_layers": [
        {
            "audio": {
                "content": "It features the westernmost point in continental Europe, and its Iberian portion is bordered to the west and south by the Atlantic Ocean and to the north and east by Spain."
            }, 
            "sets_length": True, 
            "fade_in": 1200,
            "fade_out": 1200,
        },{
            "audio": "sounds/background.mp3",
            "sets_length": False,
            "volume": 0.5
        }
    ],
    "crossfade": 2400, 
    },
]

podcast = generate(timeline)
podcast.export("podcast_4.wav", format="wav")

