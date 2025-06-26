import os
import requests

def upload_to_gofile(file_path):
    print("⬆️ Uploading video to GoFile.io...")

    try:
        # Get your GoFile account token from environment variable (optional)
        token = os.getenv("GOFILE_API_KEY")

        # Step 1: Get server
        server_res = requests.get("https://api.gofile.io/v2/getServer")
        if server_res.status_code != 200 or not server_res.text.strip():
            print("❌ Failed to get GoFile server. Empty or bad response.")
            print("🔴 Response text:", server_res.text)
            return

        server = server_res.json()['data']['server']
        print("🌐 Using server:", server)

        # Step 2: Upload file
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {'token': token} if token else {}
            response = requests.post(
                f"https://{server}.gofile.io/uploadFile",
                files=files,
                data=data
            )

        # Step 3: Check response
        if response.status_code == 200:
            res_json = response.json()
            if res_json['status'] == 'ok':
                print("✅ File uploaded!")
                print("🔗 Download link:", res_json['data']['downloadPage'])
            else:
                print("❌ Upload failed:", res_json)
        else:
            print("❌ Upload failed with status:", response.status_code, response.text)

    except Exception as e:
        print("🔥 Exception during upload:", str(e))
