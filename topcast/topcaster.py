import asyncio
from pydub import AudioSegment

from .models import Timeline, AudioContent, ChapterData
from .cutter import Cutter

class Topcaster:
    def __init__(self, timeline: Timeline):
        self.timeline = Timeline(timeline=timeline)
        self.topcast = AudioSegment.empty()
        
    def add_chapter(self, text_content=None, theme=None, tts_provider=None, audio_file=None, sets_length=True, volume=1, crossfade=0):
        chapter = {
            "audio_layers": []
        }
        
        if text_content:
            text_layer = {
                "audio": {
                    "content": text_content,
                    "theme": theme,
                    "tts_provider": tts_provider
                },
                "sets_length": sets_length
            }
            chapter["audio_layers"].append(text_layer)

        if audio_file:
            audio_layer = {
                "audio": audio_file,
                "sets_length": not sets_length,
                "volume": volume
            }
            chapter["audio_layers"].append(audio_layer)

        if crossfade:
            chapter["crossfade"] = crossfade

        self.timeline.append(chapter)
        
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
                if isinstance(audio_layer.audio, AudioContent):
                    tasks.append(
                        self.generate_text_and_assign(audio_layer)
                    )
        await asyncio.gather(*tasks)
        
    async def generate_speech(self):
        tasks = []
        
        for chapter in self.timeline.timeline:
            for audio_layer in chapter.audio_layers:
                if isinstance(audio_layer.audio, AudioContent):
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
        
    def save(self, file_name = "topcast.mp3", format="mp3"):
        self.topcast.export(file_name, format = format)
