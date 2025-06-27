import requests

def upload_to_filepush(file_path):
    print("⬆️ Uploading video to FilePush.co...")

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post("https://www.filepush.co/api/upload", files=files)

        if response.status_code == 200:
            try:
                res_json = response.json()
                if res_json.get("success"):
                    print("✅ File uploaded successfully!")
                    print("🔗 Download link:", res_json["file"]["url"])
                else:
                    print("❌ Upload failed:", res_json)
            except Exception as e:
                print("❌ Failed to parse JSON from response.")
                print("🔴 Response text:", response.text)
                print("🔥 Exception:", str(e))
        else:
            print("❌ Upload failed with status:", response.status_code)
            print("🔴 Response text:", response.text)

    except Exception as e:
        print("🔥 Exception during upload:", str(e))
