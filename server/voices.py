from google.cloud import texttospeech

VoiceMale = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    name="en-US-Neural2-J"
)

VoiceFemale = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    name="en-US-Neural2-C"
)
