import json
import os

from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"))

response = client.voices.get_all()

# Convert response to a serializable format
response_dict = {
    "voices": [
        {
            "name": voice.name,
            "voice_id": voice.voice_id,
            "category": voice.category,
            "labels": voice.labels
        } for voice in response.voices
    ]
}

# save to json
with open("voices.json", "w") as f:
    json.dump(response_dict, f, indent=2)

print(f"Saved {len(response_dict['voices'])} voices to voices.json")
