from pydub import AudioSegment
from typing import List, Dict
from .models import Timeline, StepData, AudioContent

class Cutter:
    def __init__(self, timeline: Timeline):
        self.timeline = timeline

    def cut(self):
        topcast = AudioSegment.empty()
        
        self.set_raw_audio()

        for i, step in enumerate(self.timeline.timeline):
            main_audio = None
            overlays = []

            for audio_item in step.audio_layers:
                audio = audio_item.data.raw_audio

                if audio_item.sets_length:
                    main_audio = audio
                    padding_start = AudioSegment.silent(duration=audio_item.padding_start)
                    main_audio = padding_start + main_audio
                else:
                    overlays.append(audio)
                    
            if main_audio is not None:
                step_audio = main_audio
                
                padding_end = AudioSegment.silent(duration=step.padding_end)
                step_audio = step_audio + padding_end
                
                for overlay in overlays:
                    if len(step_audio) == 0:
                        step_audio = AudioSegment.silent(duration=len(overlay))
                    step_audio = step_audio.overlay(overlay)
                    
                step_audio = step_audio.fade_in(step.fade_in)
                step_audio = step_audio.fade_out(step.fade_out)
                
                
                topcast = topcast.append(step_audio, crossfade=step.crossfade if i > 0 else 0)

        return topcast
    
    def set_raw_audio(self):
        for step in self.timeline.timeline:
            for audio_layer in step.audio_layers:
                if not isinstance(audio_layer.data.raw_audio, AudioSegment):
                    raw_audio = AudioSegment.empty()
                    
                    for audio in audio_layer.data.audio_list:
                        raw_audio = raw_audio + audio
                        
                    audio_layer.data.raw_audio = raw_audio
