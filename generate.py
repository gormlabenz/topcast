from topcast.chatgpt_themes import introduction, interview, conclusion, summary
from topcast.tts_providers import elevenlabs

timeline = [
        {
            "audio_layers": [
                {
                    "audio": 'sounds/jingle.wav', # path to audio, audio as a byte array, or a dict with the following keys: content, theme, tts_provider (default: gcp)
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                }
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "fade-out": 0, # milliseconds, how much time to fade out the audio
        },
        {
            "audio_layers": [
                {
                    "audio": {
                        "content": "LangChain is a software development framework designed to simplify the creation of applications using large language models (LLMs) such as from OpenAI, Anthropic, or Hugging Face. The framework offers a suite of tools, components, and interfaces to manage interactions with language models, chain together multiple components, and integrate resources such as APIs, databases, and a wide variety of document types. LangChain provides components for use cases such as virtual assistants, question answering about collections of documents, chatbots, querying tabular data, using APIs, and document extraction and summarization.[1]",
                        "theme": summary,
                        "tts_provider": elevenlabs
                    }, # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 1600, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 1200, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                },
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
            "fade-out": 1800,
        },         
    ]
