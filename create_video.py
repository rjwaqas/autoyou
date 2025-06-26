import requests
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from pexels_api import API
import os

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def create_video_from_images(script, audio_path, output_path):
    api = API(PEXELS_API_KEY)
    api.search(script.split()[0], results_per_page=5)
    photos = api.get_entries()

    clips = []
    for photo in photos:
        img_url = photo.original
        img_path = "img.jpg"
        with open(img_path, "wb") as f:
            f.write(requests.get(img_url).content)

        clip = ImageClip(img_path).set_duration(3)
        clips.append(clip)

    video = concatenate_videoclips(clips)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(output_path, fps=24)
