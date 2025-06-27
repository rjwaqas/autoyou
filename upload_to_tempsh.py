import subprocess
import os

def upload_to_tempsh(file_path):
    print("⬆️ Uploading video to temp.sh...")

    try:
        filename = os.path.basename(file_path)
        result = subprocess.run(
            ["curl", "--upload-file", file_path, f"https://temp.sh/{filename}"],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            print("✅ File uploaded successfully!")
            print("🔗 Download link:", result.stdout.strip())
        else:
            print("❌ Upload failed.")
            print("stderr:", result.stderr)

    except Exception as e:
        print("🔥 Exception during upload:", str(e))
