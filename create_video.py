import os
import requests
from PIL import Image  # ✅ Required for resampling fix
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from pexels_api import API

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def create_video_from_images(script, audio_path, output_path):
    if not PEXELS_API_KEY:
        raise ValueError("🚨 Missing PEXELS_API_KEY in environment variables.")

    # Initialize Pexels API
    api = API(PEXELS_API_KEY)

    # Use the first word in the script as a keyword
    keyword = script.split()[0] if script.strip() else "nature"
    print(f"🔍 Searching images for: {keyword}")
    api.search(keyword, results_per_page=5)
    photos = api.get_entries()

    if not photos:
        raise Exception("⚠️ No images found from Pexels.")

    clips = []
    for i, photo in enumerate(photos):
        img_url = photo.original
        img_path = f"temp_img_{i}.jpg"

        try:
            response = requests.get(img_url)
            with open(img_path, "wb") as f:
                f.write(response.content)

            # ✅ Create resized clip with modern resampling
            clip = ImageClip(img_path).resize(
                (1280, 720), resample=Image.Resampling.LANCZOS
            ).set_duration(3)
            clips.append(clip)

        except Exception as e:
            print(f"❌ Error downloading or processing image {img_url}: {e}")

    if not clips:
        raise Exception("❌ No clips were created, video cannot be generated.")

    # Combine all image clips and add audio
    video = concatenate_videoclips(clips)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)

    print("🎬 Writing final video...")
    video.write_videofile(output_path, fps=24)

    # Clean up temporary images
    for i in range(len(photos)):
        try:
            os.remove(f"temp_img_{i}.jpg")
        except Exception:
            pass
