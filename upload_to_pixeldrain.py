import requests
import os

def upload_to_pixeldrain(file_path):
    print("⬆️ Uploading video to PixelDrain...")

    api_key = os.getenv("PIXELDRAIN_API_KEY")
    print("🔐 API Key loaded:", bool(api_key))  # Debug print

    if not api_key:
        print("❌ PIXELDRAIN_API_KEY not set in environment.")
        return

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                "https://pixeldrain.com/api/file",
                files=files,
                auth=("user", api_key)  # required format
            )

        if response.status_code == 200:
            res_json = response.json()
            print("✅ Upload successful!")
            print(f"🔗 https://pixeldrain.com/u/{res_json['id']}")
        else:
            print("❌ Upload failed:", response.status_code)
            print("🔴 Response text:", response.text)

    except Exception as e:
        print("🔥 Exception:", str(e))
