# serve_video.py

from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ App is live! Visit /video to download the video."

@app.route("/video")
def serve_video():
    video_path = "output/output.mp4"
    if os.path.exists(video_path):
        return send_file(video_path, as_attachment=True)
    return "❌ Video not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
