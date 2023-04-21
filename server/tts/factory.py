from .gcp_provider import GCPProvider
from .elevenlabs_provider import ElevenLabsProvider

def get_tts_provider(provider_name):
    if provider_name == "gcp":
        return GCPProvider()
    elif provider_name == "elevenlabs":
        return ElevenLabsProvider()
    else:
        raise ValueError(f"Unsupported TTS provider: {provider_name}")
