from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs, GCP
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
                "content": "Portugal (Portuguese pronunciation: [puɾtuˈɣal]), officially the Portuguese Republic (Portuguese: República Portuguesa [ʁɛˈpuβlikɐ puɾtuˈɣezɐ]),[note 4] is a country located on the Iberian Peninsula, in southwestern Europe, and whose territory also includes the Atlantic archipelagos of the Azores and Madeira. It features the westernmost point in continental Europe, and its Iberian portion is bordered to the west and south by the Atlantic Ocean and to the north and east by Spain, the sole country to have a land border with Portugal. Its two archipelagos form two autonomous regions with their own regional governments. Lisbon is the capital and largest city by population.",
                "theme": Introduction,
                "tts_provider": GCP
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
podcast.export("podcast.wav", format="wav")

