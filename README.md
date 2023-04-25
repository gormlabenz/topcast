# Topcast: Turn Text into Podcasts with TTS and Language Models

Topcast is a Python package that allows you to transform text into a podcast using Text-to-Speech (TTS) and language models. With Topcast, you can provide a text, and the package will create a podcast with an introduction, interview, conclusion, sound effects, and more. Topcast supports various TTS providers and language models.

##Example Implementation

```python
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
                "tts_provider": ElevenLabs
            },
            "sets_length": True,
        }
    ],

    "crossfade": 2400,
},
]

podcast = generate(timeline)
podcast.export("podcast_3.wav", format="wav")
```

##Installation
Install the package using pip:

```bash
pip install topcast
```

##Usage

1. Import the necessary modules and set the API keys:

```python
from topcast.chatgpt_themes import Introduction, Interview, Conclusion, Summary
from topcast.tts_providers import ElevenLabs, GCP
import os
from topcast import generate, set_elevenlab_api_key, set_google_credentials, set_openai_api_key

from dotenv import load_dotenv

load_dotenv()

set_elevenlab_api_key(os.environ["ELEVENLAB_API_KEY"])
set_openai_api_key(os.environ["OPENAI_API_KEY"])
set_google_credentials('gcp-keyfile.json')
```

2. Create a timeline with the desired podcast structure:

```python
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
                "content": "Portugal...",
                "theme": Introduction,
                "tts_provider": ElevenLabs
            },
            "sets_length": True,
        }
    ],

    "crossfade": 2400,
},
]
```

3. Generate and export the podcast:

```python
podcast = generate(timeline)
podcast.export("podcast_output.wav", format="wav")
```

This will create a podcast using the given _timeline_ and save it as a WAV file named _podcast_output.wav_.
##Customization
You can customize your podcast by modifying the _timeline_ list. Each element in the list represents a segment of the podcast. You can add more segments with different themes, TTS providers, and audio layers.

For example, if you want to add an interview segment, you can include it like this:

```python
{
    "audio_layers": [
        {
            "audio": {
                "content": "Interview text...",
                "theme": Interview,
                "tts_provider": GCP
            },
            "sets_length": True,
        }
    ],
    "crossfade": 2400,
}

```

You can also add sound effects or background music by adding additional audio layers:

```python
{
    "audio_layers": [
        {
            "audio": 'sounds/background_music.wav',
            "sets_length": False,
            "volume": 0.3,
        },
        {
            "audio": {
                "content": "Text content...",
                "theme": Conclusion,
                "tts_provider": ElevenLabs
            },
            "sets_length": True,
        }
    ],
    "crossfade": 2400,
}
```

This will add background music with a volume of 0.3 to the conclusion segment.

Remember to adjust the _crossfade_ value for smoother transitions between segments.
