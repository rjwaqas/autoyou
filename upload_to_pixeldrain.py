import requests

def upload_to_pixeldrain(file_path):
    print("⬆️ Uploading video to PixelDrain...")

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post("https://pixeldrain.com/api/file", files=files)

        if response.status_code == 200:
            res_json = response.json()
            if 'id' in res_json:
                file_id = res_json['id']
                print("✅ File uploaded successfully!")
                print(f"🔗 Download link: https://pixeldrain.com/u/{file_id}")
            else:
                print("❌ Upload failed:", res_json)
        else:
            print("❌ Upload failed with status:", response.status_code)
            print("🔴 Response text:", response.text)

    except Exception as e:
        print("🔥 Exception during upload:", str(e))
