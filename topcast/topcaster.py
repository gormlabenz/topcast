import asyncio
from pydub import AudioSegment

from .models import Timeline, AudioItem, ChapterData, Chapter
from .cutter import Cutter

class Topcaster:
    def __init__(self, timeline: Timeline = []):
        self.timeline = Timeline(timeline=timeline)
        self.topcast = AudioSegment.empty()
        
    def add_chapter(self, audio_layers = [], fade_in: int = 1, fade_out: int = 1 , padding_start: int = 0 , padding_end: int = 0 , crossfade: int = 0, volume: float = 1):
        
        chapter = Chapter(audio_layers=audio_layers, fade_in=fade_in, fade_out=fade_out, padding_start=padding_start, padding_end=padding_end, crossfade=crossfade, volume=volume)
        self.timeline.timeline.append(chapter)
        
    def generate(self):
        self.add_chapter_data_dict()
        self.open_audio_files()
        asyncio.run(self.generate_text())
        asyncio.run(self.generate_speech())
        self.cut()
        
        return self.topcast

    def add_chapter_data_dict(self):
        for chapter in self.timeline.timeline:
            for audio_layer in chapter.audio_layers:
                audio_layer.data = ChapterData(raw_audio= None, text_list=[], audio_list= [])
                
    def open_audio_files(self):
        for chapter in self.timeline.timeline:
            for audio_layer in chapter.audio_layers:
                if type(audio_layer.audio) == str:
                    audio_layer.data.raw_audio = AudioSegment.from_file(audio_layer.audio)              

    async def generate_text(self):
        tasks = []
        for chapter in self.timeline.timeline:
            for audio_layer in chapter.audio_layers:
                if isinstance(audio_layer.audio, AudioItem):
                    tasks.append(
                        self.generate_text_and_assign(audio_layer)
                    )
        await asyncio.gather(*tasks)
        
    async def generate_speech(self):
        tasks = []
        
        for chapter in self.timeline.timeline:
            for audio_layer in chapter.audio_layers:
                if isinstance(audio_layer.audio, AudioItem):
                    tasks.append(self.generate_speech_and_assign(audio_layer))
                    
        await asyncio.gather(*tasks)
        
    def cut(self):
        
        topcast =  Cutter(self.timeline).cut()
        self.topcast = topcast
    
    async def generate_text_and_assign(self, audio_layer):
        chatgpt_theme = audio_layer.audio.theme()
        
        generated_text = await chatgpt_theme.create_chat_completion(audio_layer.audio.content)
        
        audio_layer.data.text_list = generated_text
        
    async def generate_speech_and_assign(self, audio_layer):
        provider = audio_layer.audio.tts_provider()
        tasks = []
        
        for text in audio_layer.data.text_list:
            tasks.append(
                provider.tts(text)
            )
            
            
        results = await asyncio.gather(*tasks)        
        audio_layer.data.audio_list = results
        
    def export(self, file_name = "topcast.mp3", format="mp3"):
        self.topcast.export(file_name, format = format)
