from pydub import AudioSegment
from typing import List, Dict
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
                audio = audio_item.data.raw_audio

                if audio_item.sets_length:
                    main_audio = audio
                    padding_start = AudioSegment.silent(duration=audio_item.padding_start)
                    main_audio = padding_start + main_audio
                else:
                    overlays.append(audio)
                    
            if main_audio is not None:
                chapter_audio = main_audio
                
                padding_end = AudioSegment.silent(duration=chapter.padding_end)
                chapter_audio = chapter_audio + padding_end
                
                for overlay in overlays:
                    if len(chapter_audio) == 0:
                        chapter_audio = AudioSegment.silent(duration=len(overlay))
                    chapter_audio = chapter_audio.overlay(overlay)
                    
                chapter_audio = chapter_audio.fade_in(chapter.fade_in)
                chapter_audio = chapter_audio.fade_out(chapter.fade_out)
                
                
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
