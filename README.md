# Topcast: The Open-Source Alternative to Google NotebookLM Audio Overview

Topcast is an open-source Python package that transforms your text into engaging podcast-like audio, much like Google NotebookLM's new "Audio Overview" feature. While Google NotebookLM turns documents and slides into conversations, Topcast gives you the freedom to create podcasts from any text using Text-to-Speech (TTS) and language models, adding layers of sound, structure, and effects to create a comprehensive audio experience.

https://github.com/user-attachments/assets/88f8d774-7f4d-4f39-b646-1238d689d3c6

## What is Topcast?

With Topcast, you can provide a text, and the package will generate a dynamic audio output that includes introductions, interviews, conclusions, and more. It supports multiple TTS providers and AI-powered language models like ChatGPT to make your podcast rich and diverse. The key difference? Topcast is fully open-source, and you have complete control over the customization of your audio content.

### Key Features

- **Customizable Audio Layers**: Combine TTS, sound effects, and more to create rich audio experiences.
- **ChatGPT Themes**: Easily transform text into interview-style conversations, summaries, introductions, or conclusions.
- **Multiple TTS Providers**: Choose from Google Cloud, Elevenlabs, or Google Translate TTS, allowing flexibility in voice quality and pricing.
- **Open-Source and Transparent**: Unlike commercial solutions, you can modify and extend Topcast as per your needs. Your data is your own, and nothing is used without your explicit consent.

## Example Implementation

```python
from topcast import Topcaster, set_openai_api_key
from topcast.chatgpt_themes import Introduction

set_openai_api_key("XXX-XXX-XXX-XXX-XXX")

topcast = Topcaster()

topcast.add_chapter(audio_layers=[{ "audio" : "sounds/jingle.wav" }])
topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "Topcast is a Python package that allows you to transform text into a podcast using Text-to-Speech (TTS) and language models. With Topcast, you can provide a text, and the package will create a podcast with an introduction, interview, conclusion, sound effects, and more. Topcast supports various TTS providers and language models.",
                "theme": Introduction,
            },
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
    set_elevenlabs_api_key,
    set_google_credentials,
    set_openai_api_key,
    Topcaster,
)

from topcast.tts_providers import GCP
from topcast.chatgpt_themes import Summary

set_elevenlabs_api_key("XXX-XXX-XXX") # if you want to use elvenlabs for tts
set_google_credentials("gcp-keyfile.json") # if you want google cloud platform for tts
set_openai_api_key("XXX-XXX-XXX") # if you want to use a ChatGPT theme
```

2. Create a Topcaster object and add chapters with the desired podcast structure:

```python
topcast = Topcaster()

topcast.add_chapter(
    audio_layers=[
        {
            "audio": "sounds/jingle.wav", # use a audio file
            "sets_length": True,
        }
    ]
)
topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "Portugal...",
                "tts_provider": GCP, # use google cloud platform for tts
                "theme": Summary, # generate a summary of the text using ChatGPT
            },
            "sets_length": True, # this audio_layer sets the length of the chapter, only one audio_layer can set the length per chapter
            "fade_in": 1200, # fade in 1200 ms
            "fade_out": 1200, # fade out 1200 ms
        },
        {"audio": "sounds/background.mp3", "sets_length": False, "volume": 0.5}, # overlay audio
    ],
    crossfade=2400, # crossfade last chapter
)

```

3. Generate and export the podcast:

```python
topcast.generate()
topcast.export("podcast.wav", format="wav")
```

This will create a podcast using the given chapters and save it as a WAV file named podcast_output.wav.

## ChatGPT Themes

ChatGPT Themes allow you to transform your text into various structures by leveraging ChatGPT, a large language model. With the available themes, you can transform your text into an interview, introduction, summary, or conclusion. You can also choose to leave the text as it is by using the NoneTheme, which is the default theme.

The available ChatGPT Themes are:

- Interview
- Introduction
- Summary
- Conclusion
- NoneTheme (default)

### Usage

To use a specific ChatGPT theme, first import the desired theme:

```python
from topcast.chatgpt_themes import Interview, Introduction, Summary, Conclusion
```

Then, set your OpenAI API key using the set_openai_api_key function:

```python
from topcast import set_openai_api_key

set_openai_api_key("your-openai-api-key")

```

Finally, set the `theme` property in the audio layer of the desired chapter:

```python
{
    "audio": {
        "content": "Text content...",
        "theme": Introduction,  # Replace with the desired theme
    },
}

```

To keep the original text without any transformation, set NoneTheme or don't set `theme` at all

```python
from topcast.chatgpt_themes import NoneTheme

{
    "audio": {
        "content": "Text content...",
        "theme": NoneTheme,  # Keeps the text as it is
    },
}
```

## TTS Providers

Topcast allows you to use various Text-to-Speech (TTS) providers to convert your text into speech. The currently implemented TTS providers are:

- GCP (Google Cloud Platform) - Requires a Google Cloud Platform account
- Elevenlabs - Requires an Elevenlabs account
- GTTS (Google Translate) - No account required (default)

### Comparison

- **Elevenlabs**: Offers the best voices but is expensive and has API limits.
- **GCP (Google Cloud Platform)**: Relatively cheap but requires a Google Cloud Platform account with the Text-to-Speech API enabled.
- **GTTS (Google Translate)**: Free and does not require an account, but the voice quality is not as good as the other options.

### Usage

First, import the desired TTS provider:

```python
from topcast.tts_providers import GCP, Elevenlabs, GTTS

```

Next, set the API key or credentials for the provider, if required:

```python
from topcast import set_elevenlabs_api_key, set_google_credentials

set_elevenlabs_api_key("your-elevenlabs-api-key")
set_google_credentials("path-to-gcp-keyfile.json")
```

Finally, specify the tts_provider property in the audio layer of the desired chapter:

```python
{
    "audio": {
        "content": "Text content...",
        "tts_provider": GCP,  # Replace with the desired TTS provider
    },
}

```

For example, to create a chapter using the GCP TTS provider:

```python
topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "Text content...",
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

```

To use the default GTTS provider, you can simply omit the tts_provider property:

```python
{
    "audio": {
        "content": "Text content...",
    },
}
```

## Why Topcast?

If you're looking for a free, open-source alternative to tools like Google NotebookLM, Topcast gives you the freedom to create personalized audio content without platform restrictions. Whether it's for study, entertainment, or work, Topcast puts the power of AI and audio creation in your hands.
