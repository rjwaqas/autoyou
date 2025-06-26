from generate_script import generate_script
from create_video import create_video_from_images
from text_to_speech import convert_text_to_speech

if __name__ == "__main__":
    title = input("Enter a YouTube video title: ")

    script = generate_script(title)
    convert_text_to_speech(script, "voice.mp3")
    create_video_from_images(script, "voice.mp3", "output.mp4")

    print("🎥 Video created: output.mp4")
