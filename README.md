
# Topcast
## The Open-Source Alternative to Google NotebookLM Audio Overview

Topcast is an open-source Python package that transforms your text into engaging podcast-like audio, much like Google NotebookLM's new "Audio Overview" feature. While Google NotebookLM turns documents and slides into conversations, Topcast gives you the freedom to create podcasts from any text using Text-to-Speech (TTS) and language models, adding layers of sound, structure, and effects to create a comprehensive audio experience.

## What is Topcast?
With Topcast, you can provide a text, and the package will generate a dynamic audio output that includes introductions, interviews, conclusions, and more. It supports multiple TTS providers and AI-powered language models like ChatGPT to make your podcast rich and diverse. The key difference? Topcast is fully open-source, and you have complete control over the customization of your audio content.

### Key Features
- **Customizable Audio Layers**: Combine TTS, sound effects, and more to create rich audio experiences.
- **ChatGPT Themes**: Easily transform text into interview-style conversations, summaries, introductions, or conclusions.
- **Multiple TTS Providers**: Choose from Google Cloud, Elevenlabs, or Google Translate TTS, allowing flexibility in voice quality and pricing.
- **Open-Source and Transparent**: Unlike commercial solutions, you can modify and extend Topcast as per your needs. Your data is your own, and nothing is used without your explicit consent.

## Example Podcast
Generated using ChatGPT themes: Introduction with the ElevenLabs TTS Provider, Interview with the GCP TTS Provider, and Summary with ElevenLabs TTS Provider.

[Video example of generated podcast]

## How to Get Started

1. Install Topcast:
   ```bash
   pip install topcast
   ```

2. Configure your API keys and set up your TTS providers:
   ```python
   from topcast import set_elevenlab_api_key, set_google_credentials, set_openai_api_key
   set_elevenlab_api_key("XXX-XXX-XXX")
   set_google_credentials("gcp-keyfile.json")
   set_openai_api_key("XXX-XXX-XXX")
   ```

3. Create a new Topcast instance and add chapters to build your podcast:
   ```python
   topcast = Topcaster()
   topcast.add_chapter(audio_layers=[{"audio": "sounds/jingle.wav"}])
   topcast.add_chapter(audio_layers=[{"audio": {"content": "Your text...", "tts_provider": GCP, "theme": Summary}}])
   ```

4. Generate and export your podcast:
   ```python
   topcast.generate()
   topcast.export("podcast.wav", format="wav")
   ```

## Why Topcast?
If you're looking for a free, open-source alternative to tools like Google NotebookLM, Topcast gives you the freedom to create personalized audio content without platform restrictions. Whether it's for study, entertainment, or work, Topcast puts the power of AI and audio creation in your hands.
