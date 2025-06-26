import requests

def upload_to_fileio(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post("https://file.io", files={"file": f})
    
    if response.status_code == 200:
        print("✅ File uploaded!")
        print("🔗 Download link:", response.json()['link'])
    else:
        print("❌ Upload failed:", response.text)
