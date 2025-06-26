from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ App is live! Go to /video to download your video."

@app.route('/video')
def serve_video():
    video_path = "output/output.mp4"
    if os.path.exists(video_path):
        return send_file(video_path, as_attachment=True)
    else:
        return "❌ Video not found. Please run main.py first to generate it.", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
