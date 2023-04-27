from pydub import AudioSegment
from typing import List, Dict, Union
from .models import Timeline, ChapterData, AudioItem

class Cutter:
    def __init__(self, timeline: Timeline):
        self.timeline = timeline

    def cut(self):
        topcast = AudioSegment.empty()
        
        self.set_raw_audio()

        for i, chapter in enumerate(self.timeline.timeline):
            main_audio = None
            overlays = []
            
            for audio_item in chapter.audio_layers:
                if audio_item.sets_length:
                    audio = self.add_effects(audio_item.data.raw_audio, audio_item)
                    main_audio = audio
                
            for audio_item in chapter.audio_layers:
                if not audio_item.sets_length:
                    audio = self.add_effects(audio_item.data.raw_audio[:len(main_audio)], audio_item)
                    overlays.append(audio)
                
            if main_audio is not None:
                chapter_audio = main_audio
                                
                for overlay in overlays:
                    chapter_audio = chapter_audio.overlay(overlay)
                
                chapter_audio = self.add_effects(chapter_audio, chapter)
                
                topcast = topcast.append(chapter_audio, crossfade=chapter.crossfade if i > 0 else 0)

        return topcast
    
    def set_raw_audio(self):
        for chapter in self.timeline.timeline:
            for audio_layer in chapter.audio_layers:
                if not isinstance(audio_layer.data.raw_audio, AudioSegment):
                    raw_audio = AudioSegment.empty()
                    
                    for audio in audio_layer.data.audio_list:
                        raw_audio = raw_audio + audio
                        
                    audio_layer.data.raw_audio = raw_audio

    def add_effects(self, audio: AudioSegment, audio_item: Union[AudioItem, ChapterData]):
        padding_start = AudioSegment.silent(duration=audio_item.padding_start)
        padding_end = AudioSegment.silent(duration=audio_item.padding_end)
        
        audio = padding_start + audio + padding_end

        audio = audio.fade_in(audio_item.fade_in)
        audio = audio.fade_out(audio_item.fade_out)

        # audio = audio.apply_gain(audio_item.volume)
        return audio
