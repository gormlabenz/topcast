import asyncio
from .models import Timeline, AudioContent, StepData
from .chatgpt import ChatGPT
from pydub import AudioSegment

class Podcaster:
    def __init__(self, timeline: Timeline):
        self.timeline = Timeline(timeline=timeline).timeline
        
    def generate(self):
        self.add_step_data_dict()
        self.open_audio_files()
        asyncio.run(self.generate_text())
        asyncio.run(self.generate_speech())
        
        return self.timeline

    def add_step_data_dict(self):
        for step in self.timeline:
            for audio_layer in step.audio_layers:
                audio_layer.data = StepData(raw_audio= None, text_list=[], audio_list= [])
                
    def open_audio_files(self):
        for step in self.timeline:
            for audio_layer in step.audio_layers:
                if type(audio_layer.audio) == str:
                    audio_layer.data.raw_audio = AudioSegment.from_file(audio_layer.audio)

    async def generate_text(self):
        tasks = []
        for step in self.timeline:
            for audio_layer in step.audio_layers:
                if isinstance(audio_layer.audio, AudioContent):
                    tasks.append(
                        self.generate_text_and_assign(audio_layer)
                    )
        await asyncio.gather(*tasks)
        
    async def generate_speech(self):
        tasks = []
        for step in self.timeline:
            for audio_layer in step.audio_layers:
                if isinstance(audio_layer.audio, AudioContent):
                    tasks.append(self.generate_speech_and_assign(audio_layer))
                    
        await asyncio.gather(*tasks)

    async def generate_text_and_assign(self, audio_layer):
        chatgpt = ChatGPT(audio_layer.audio)
        generated_text = await chatgpt.create_chat_completion(audio_layer.audio.content)
        audio_layer.data.text_list = generated_text
        
    async def generate_speech_and_assign(self, audio_layer):
        provider = audio_layer.audio.tts_provider()
        tasks = []
        
        for text in audio_layer.data.text_list:
            tasks.append(
                provider.tts(text)
            )
            
        await asyncio.gather(*tasks)
        
        audio_layer.data.audio_list = tasks
