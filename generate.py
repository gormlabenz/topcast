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
