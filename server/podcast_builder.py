from pydub import AudioSegment
from typing import List, Dict

class PodcastBuilder:
    def __init__(self, timeline: List[Dict]):
        self.timeline = timeline

    def build(self, output_file: str = "podcast.wav"):
        podcast = AudioSegment.empty()

        for step in self.timeline:
            main_audio = None
            overlays = []

            for audio_item in step["audio"]:
                audio = AudioSegment.from_file(audio_item["audio"])

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
                    step_audio = step_audio.overlay(overlay)
                    

                
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
      
      
timeline = [
    {
        "audio": [
            {
                "audio": 'sounds/jingle.wav', # audio as a byte array,
                "is_main": True, # if True, this audio sets the length of the step in the timeline
                "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                "volume": 1 # volume of the audio, 1 is normal, 0 is muted
            }
        ],
     
        "fade-in": 0, # milliseconds, how much time to fade in the audio
        "fade-out": 0, # milliseconds, how much time to fade out the audio
    },
        {
        "audio": [
            {
                "audio": 'sounds/output.wav', # audio as a byte array,
                "is_main": True, # if True, this audio sets the length of the step in the timeline
                "padding_start": 2800, # milliseconds, how much time to add before the audio gets played
                "padding_end": 1800, # milliseconds, how much time to add after the audio gets played
                 "volume": 1 # volume of the audio, 1 is normal, 0 is muted
            },
            {
                "audio": 'sounds/background.mp3', # audio as a byte array,
                "is_main": False, # if True, this audio sets the length of the step in the timeline
                "padding_start": 0, # milliseconds, how much time to add before the audio gets played
                "padding_end": 0, # milliseconds, how much time to add after the audio gets played
                 "volume": 0.2 # volume of the audio, 1 is normal, 0 is muted
            }
        ],
        "fade-in": 0, # milliseconds, how much time to fade in the audio
        "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
        "fade-out": 1800,
    }
]

# Example usage:
builder = PodcastBuilder(timeline)
output_file = builder.build()
print(f"The podcast has been generated and saved to {output_file}.")
