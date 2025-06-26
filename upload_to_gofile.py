import requests

def upload_to_gofile(file_path):
    print("⬆️ Uploading video to GoFile.io...")

    # Get the best server
    server_res = requests.get("https://api.gofile.io/getServer")
    server = server_res.json()['data']['server']

    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(
            f"https://{server}.gofile.io/uploadFile",
            files=files
        )

    if response.status_code == 200:
        res_json = response.json()
        if res_json['status'] == 'ok':
            download_link = res_json['data']['downloadPage']
            print("✅ File uploaded!")
            print("🔗 Download link:", download_link)
        else:
            print("❌ Upload failed:", res_json)
    else:
        print("❌ Upload failed:", response.status_code, response.text)
