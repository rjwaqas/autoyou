import requests

def upload_to_gofile(file_path):
    print("⬆️ Uploading video to GoFile.io...")

    try:
        server_res = requests.get("https://api.gofile.io/v2/getServer")
        if server_res.status_code != 200 or not server_res.text.strip():
            print("❌ Failed to get GoFile server. Empty or bad response.")
            print("🔴 Response text:", server_res.text)
            return

        server = server_res.json()['data']['server']
        print("🌐 Using server:", server)

        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                f"https://{server}.gofile.io/uploadFile",
                files=files
            )

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
