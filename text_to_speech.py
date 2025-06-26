from gtts import gTTS

def convert_text_to_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)
