from topcast import Topcaster, set_elevenlab_api_key, set_openai_api_key
from topcast.chatgpt_themes import Summary
from topcast.tts_providers import GTTS, ElevenLabs

topcast = Topcaster()

# topcast.add_chapter(audio_layers=[{"audio": "sounds/jingle.wav"}])
topcast.add_chapter(
    audio_layers=[
        {
            "audio": {
                "content": "Topcast is a Python package that allows you to transform text into a podcast using Text-to-Speech (TTS) and language models. With Topcast, you can provide a text, and the package will create a podcast with an introduction, interview, conclusion, sound effects, and more. Topcast supports various TTS providers and language models.",
                "theme": Summary,
                "tts_provider": ElevenLabs
            },
        },
    ],
)

topcast.generate()
topcast.export("podcast_topcast.wav", format="wav")
