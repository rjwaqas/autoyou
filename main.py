print("🚀 App started")

import os
from generate_script import generate_script
from create_video import create_video_from_images
from text_to_speech import convert_text_to_speech
from upload_to_fileio import upload_to_fileio

if __name__ == "__main__":
    title = os.getenv("YOUTUBE_TITLE", "Default Video Title")

    # 1. Generate script
    script = generate_script(title)

    # 2. Convert text to speech
    convert_text_to_speech(script, "voice.mp3")

    # 3. Create video from images and audio
    create_video_from_images(script, "voice.mp3", "output/output.mp4")

    print("🎥 Video created at: output/output.mp4")

    # 4. Upload video to file.io
    upload_to_fileio("output/output.mp4")
