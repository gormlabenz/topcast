from topcast.models import AudioContent
from topcast.chatgpt_themes import Interview
from topcast.tts_providers import ElevenLabs

try:
    audio_content = AudioContent(
        content="Hello world",
        theme=Interview,
        tts_provider=ElevenLabs
    )
    print("AudioContent is valid!")
except ValueError as e:
    print(f"AudioContent validation error: {e}")
