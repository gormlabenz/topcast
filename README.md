# Topcast: Turn Text into Podcasts with TTS and Language Models

Topcast is a Python package that allows you to transform text into a podcast using Text-to-Speech (TTS) and language models. With Topcast, you can provide a text, and the package will create a podcast with an introduction, interview, conclusion, sound effects, and more. Topcast supports various TTS providers and language models.

## Example Implementation

```python
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

```

## Installation
Install the package using pip:

```bash
pip install topcast
```

## Usage

1. Import the necessary modules and set the API keys:

```python
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
```

2. Create a Topcaster object and add chapters with the desired podcast structure:

```python
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
                "content": "Portugal...",
                "tts_provider": GCP,
                "theme": Summary,
            },
            "sets_length": True,
            "fade_in": 1200,
            "fade_out": 1200,
        },
        {"audio": "sounds/background.mp3", "sets_length": False, "volume": 0.5},
    ],
    crossfade=2400,
)

```

3. Generate and export the podcast:

```python
topcast.generate()
topcast.export("podcast_output.wav", format="wav")
```
This will create a podcast using the given chapters and save it as a WAV file named podcast_output.wav.
##Customization
You can customize your podcast by adding more chapters to the Topcaster object. Each chapter represents a segment of the podcast. You can add more segments with different themes, TTS providers, and audio layers.

For example, if you want to add an interview segment, you can include it like this:

```python
from topcast import Topcaster
from topcast.chatgpt_themes import Interview

topcast = Topcast()

topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "It features the westernmost point in continental Europe, and its Iberian portion is bordered to the west and south by the Atlantic Ocean and to the north and east by Spain...", # <- gets automatically converted into an interview script
                "tts_provider": GCP,
                "theme": Interview,
            },
            "sets_length": True,
            "fade_in": 1200,
            "fade_out": 1200,
        },
    ],
    crossfade=2400,
)


```

You can also add sound effects or background music by adding additional audio layers within a chapter:

```python
from topcast import Topcaster

topcast = Topcast()

topcast.add_chapter(
    audio_layers=[
        {
            "audio": 'sounds/background_music.wav',
            "sets_length": False,
            "volume": 0.3,
        },
        {
            "audio": {
                "content": "Text content...",
                "tts_provider": GCP,
                "theme": Summary,
            },
            "sets_length": True,
            "fade_in": 1200,
            "fade_out": 1200,
        }
    ],
    crossfade=2400,
)
```
This will add background music with a volume of 0.3 to the chapter.

Remember to adjust the crossfade value for smoother transitions between chapters.
