import requests
import os

def upload_to_tempsh(file_path):
    print("⬆️ Uploading video to temp.sh...")

    try:
        filename = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            response = requests.put(f"https://temp.sh/{filename}", data=f)

        if response.status_code == 200:
            download_link = response.text.strip()
            print("✅ File uploaded successfully!")
            print("🔗 Download link:", download_link)
        else:
            print("❌ Upload failed with status:", response.status_code)
            print("🔴 Response text:", response.text)

    except Exception as e:
        print("🔥 Exception during upload:", str(e))
