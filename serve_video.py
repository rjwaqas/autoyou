from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Video Generator is Running. Go to /video to download the latest video."

@app.route('/video')
def download_video():
    return send_file('output/output.mp4', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
