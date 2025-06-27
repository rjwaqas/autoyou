import requests

def upload_to_transfersh(file_path):
    print("⬆️ Uploading video to transfer.sh...")

    try:
        with open(file_path, 'rb') as f:
            response = requests.put(f'https://transfer.sh/{file_path}', data=f)

        if response.status_code == 200:
            print("✅ File uploaded successfully!")
            print("🔗 Download link:", response.text.strip())
        else:
            print("❌ Upload failed:", response.status_code, response.text)

    except Exception as e:
        print("🔥 Exception during upload:", str(e))
