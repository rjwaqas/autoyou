# serve_video.py
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Your app is live! Visit /video to download the video."

@app.route('/video')
def download_video():
    path = "output/output.mp4"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    else:
        return "❌ Video not found. Please generate it first.", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
