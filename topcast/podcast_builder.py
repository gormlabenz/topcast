from pydub import AudioSegment
from typing import List, Dict
from io import BytesIO

class PodcastBuilder:
    def __init__(self, timeline: List[Dict]):
        self.timeline = timeline

    def build(self, output_file: str = "podcast.wav"):
        podcast = AudioSegment.empty()

        for step in self.timeline:
            main_audio = None
            overlays = []

            for audio_item in step["audio"]:
                if type(audio_item["audio"]) == str:
                    audio = AudioSegment.from_file(audio_item["audio"])
                else:
                    audio = audio_item["audio"]

                if audio_item["is_main"]:
                    main_audio = audio
                    padding_start = AudioSegment.silent(duration=audio_item["padding_start"])
                    main_audio = padding_start + main_audio
                else:
                    overlays.append(audio)
                    
            if main_audio is not None:
                step_audio = main_audio
                
                padding_end = AudioSegment.silent(duration=step["audio"][0]["padding_end"])
                step_audio = step_audio + padding_end
                
                for overlay in overlays:
                    if len(step_audio) == 0:
                        step_audio = AudioSegment.silent(duration=len(overlay))
                    step_audio = step_audio.overlay(overlay, loop=True)
                    

                
                if step.get("fade-in"):
                    step_audio = step_audio.fade_in(step["fade-in"])

                if step.get("fade-out"):
                    step_audio = step_audio.fade_out(step["fade-out"])

                if step.get("overlapping"):
                    podcast = podcast.append(step_audio, crossfade=step["overlapping"])
                else:
                    podcast = podcast.append(step_audio,crossfade=0)
                    
                

        podcast.export(output_file, format="wav")
        return output_file
      
    
