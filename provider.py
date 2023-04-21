import asyncio
from io import BytesIO
from pydub import AudioSegment
from server.tts.elevenlabs_provider import ElevenLabsProvider
from server.podcast_chunk import run_tasks

text_items = [{'text': 'Welcome to our program today! Today we have a special guest who is an expert on the history of ancient Scandinavia. Please welcome Mr. Norse. Mr. Norse, today we want to discuss King Gorm from Denmark. Can you tell us more about him?', 'gender': 'male'}, {'text': 'Of course, thank you for having me! King Gorm was a semi-legendary Danish king who ruled in the 10th century. According to Adam of Bremen, his father Harthacnut came to Denmark from Northmannia and overthrew the young king Sigtrygg Gnupasson to take power over Western Denmark. When Harthacnut died, Gorm ascended the throne.', 'gender': 'female'}, {'text': "That's interesting! How did Gorm come to power and what kind of ruler was he?", 'gender': 'male'}, {'text': "Gorm is believed to have taken at least part of the kingdom by force from Sigtrygg Gnupasson, and some say that the kingdom was already divided before Gorm's reign. He is not extensively documented, but our knowledge of him comes from his hosting of Archbishop Unni of Hamburg and Bremen in the year 936. Gorm is also known for being the father of the famous King Harald Bluetooth, who is credited with unifying all of Denmark.", 'gender': 'female'}, {'text': "That's fascinating! What can you tell us about Jelling, the seat of Gorm's power?", 'gender': 'male'}, {'text': "Gorm is known to have ruled from Jelling, a village in Jutland, Denmark. The Jelling Stones, which were erected by Gorm's son Harald in honor of his parents, mention Gorm's achievements and his descendants. It is believed that Gorm only ruled over Jutland from his seat in Jelling, while his son Harald expanded the kingdom and became a more famous ruler.", 'gender': 'female'}, {'text': "That's great to know! Although Gorm's reign is not well-documented, his legacy through his son Harald Bluetooth is significant. How did Gorm contribute to the legacy of Danish kingship?", 'gender': 'male'}, {'text': "Gorm is credited for laying the foundation of the Danish monarchy, and setting the stage for his son Harald to create a unified kingdom. The Jelling Stones are an important artifact of his reign, being the first official documentation of a Danish king. Gorm's legacy is also evident in his descendants, who continue to rule Denmark for centuries to come.", 'gender': 'female'}, {'text': "Thank you, Mr. Norse, for sharing your knowledge of the history of Denmark, and the significance of King Gorm. It's intriguing to see how the foundation of Danish monarchy was built, with Gorm as a crucial figure.", 'gender': 'male'}]

async def main():
    text = "Next click on the eye icon on your profile to access your xi-api-key."
    gender = "male"

    tts_provider = ElevenLabsProvider()
    
    tasks = [
        asyncio.create_task(tts_provider.tts(text = text_item["text"], gender = text_item["gender"])) for text_item in text_items
        ] 
    
    
    speech_results = await run_tasks(tasks, run_async = False)
    
    combined_audio = AudioSegment.empty()
    # Saving the speech_result to a file
    for speech in speech_results:
            # Convert the audio_content (bytes) to an AudioSegment
            audio_segment = AudioSegment.from_file(BytesIO(speech))
            
            # Concatenate the current audio segment with the combined_audio
            combined_audio += audio_segment

    # Load the saved file and play it
    combined_audio.export("output_8.wav", format="wav")

if __name__ == "__main__":
    asyncio.run(main())
