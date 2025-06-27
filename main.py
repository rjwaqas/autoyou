print("🚀 App started")

import os
from generate_script import generate_script
from create_video import create_video_from_images
from text_to_speech import convert_text_to_speech
from upload_to_transfersh import upload_to_transfersh  # ✅ Corrected import

if __name__ == "__main__":
    title = os.getenv("YOUTUBE_TITLE", "Default Video Title")

    # 1. Generate script
    script = generate_script(title)

    # 2. Convert text to speech
    convert_text_to_speech(script, "voice.mp3")

    # 3. Create video from images and voice
    create_video_from_images(script, "voice.mp3", "output/output.mp4")

    print("🎥 Video created at: output/output.mp4")

    # 4. Upload video to transfer.sh
   upload_to_transfersh("output/output.mp4")
