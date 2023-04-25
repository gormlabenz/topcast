import os
from topcast import (
    set_elevenlab_api_key,
    set_google_credentials,
    set_openai_api_key,
    Topcaster,
)

from topcast.tts_providers import GCP
from topcast.chatgpt_themes import Summary

from dotenv import load_dotenv

load_dotenv()

set_elevenlab_api_key(os.environ["ELEVENLAB_API_KEY"])
set_openai_api_key(os.environ["OPENAI_API_KEY"])
set_google_credentials("gcp-keyfile.json")

topcast = Topcaster()

topcast.add_chapter(
    audio_layers=[
        {
            "audio": "sounds/jingle.wav",
            "sets_length": True,
        }
    ]
)
topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "It features the westernmost point in continental Europe, and its Iberian portion is bordered to the west and south by the Atlantic Ocean and to the north and east by Spain.",
            },
            "sets_length": True,
            "fade_in": 1200,
            "fade_out": 1200,
        },
        {"audio": "sounds/background.mp3", "sets_length": False, "volume": 0.5},
    ],
    crossfade=2400,
)
topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "It features the westernmost point in continental Europe, and its Iberian portion is bordered to the west and south by the Atlantic Ocean and to the north and east by Spain.",
                "tts_provider": GCP, 
                "theme": Summary,
            },
            "sets_length": True,
            "fade_in": 1200,
            "fade_out": 1200,
        },
    ],
    crossfade=2400,
)

topcast.generate()
topcast.export("podcast.wav", format="wav")
