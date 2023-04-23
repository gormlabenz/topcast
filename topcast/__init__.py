from .podcaster import Podcaster
from .models import Timeline

def generate(timeline: Timeline):
    podcaster = Podcaster(timeline)
    podcast = podcaster.generate()
    return podcast
