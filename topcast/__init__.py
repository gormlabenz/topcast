from .podcaster import Podcaster
from .models import Timeline

def generate(timeline: Timeline):
    podcaster = Podcaster(timeline)
    podcast = podcaster.generate()
    return podcast

def set_elevenlab_api_key(api_key: str):
    from elevenlabs import set_api_key
    set_api_key(api_key)

def set_openai_api_key(api_key: str):
    import openai
    openai.api_key = api_key

def set_google_credentials(filename: str):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = filename
