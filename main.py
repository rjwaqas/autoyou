from generate_script import generate_script
from create_video import create_video_from_images
from text_to_speech import convert_text_to_speech
import os

if __name__ == "__main__":
    title = os.getenv("YOUTUBE_TITLE", "Default Video Title")
    script = generate_script(title)
    convert_text_to_speech(script, "voice.mp3")
    create_video_from_images(script, "voice.mp3", "output/output.mp4")
    print("🎥 Video created at: output/output.mp4")

import shutil
import os

# Create static folder if not exists
os.makedirs("static", exist_ok=True)

# Copy video to static
shutil.copy("output/output.mp4", "static/output.mp4")

print("✅ Video copied to static/output.mp4. Access it via /static/output.mp4")
