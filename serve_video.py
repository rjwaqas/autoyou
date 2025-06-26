from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return "<h2>✅ Video Ready: <a href='/static/output.mp4'>Download Video</a></h2>"

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
