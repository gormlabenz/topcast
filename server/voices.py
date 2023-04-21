from google.cloud import texttospeech

voiceMale = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    name="en-US-Neural2-J"
)

voiceFemail = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    name="en-US-Neural2-C"
)
