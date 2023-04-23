from .base_timeline import Timeline

class LongTimeline(Timeline):
    def get_timeline(audio_list: list):
        if len(audio_list) != 3:
            raise Exception("The number of audio files must be 3")
        
        return [
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
                    "audio": audio_list[0], # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 2600, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 1200, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                },
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
            "fade-out": 1800,
        },
            {
            "audio": [
                {
                    "audio": audio_list[1], # audio as a byte array,
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
        },
            {
            "audio": [
                {
                    "audio": audio_list[2], # audio as a byte array,
                    "is_main": True, # if True, this audio sets the length of the step in the timeline
                    "padding_start": 2800, # milliseconds, how much time to add before the audio gets played
                    "padding_end": 1800, # milliseconds, how much time to add after the audio gets played
                    "volume": 1 # volume of the audio, 1 is normal, 0 is muted
                }
            ],
            "fade-in": 0, # milliseconds, how much time to fade in the audio
            "overlapping": 2400, # milliseconds, how much time to overlap the audio with the step before
            "fade-out": 1800,
        }
            
    ]

