import requests

# Your current proxy and key
YTPROXY_URL = "https://ytproxy-marwin-bbc2658d0713.herokuapp.com"
YT_API_KEY = "marwinsecretkey2002"

# Test with any YouTube video ID
video_id = "dQw4w9WgXcQ"  # you can change to any

headers = {"x-api-key": YT_API_KEY}

try:
    print("🔍 Checking your API key...")
    resp = requests.get(f"{YTPROXY_URL}/info/{video_id}", headers=headers, timeout=10)
    print(f"HTTP {resp.status_code}")
    try:
        data = resp.json()
    except Exception:
        print("❌ Invalid JSON or empty response:")
        print(resp.text)
        exit()

    if data.get("status") == "success":
        print("✅ API key is valid and working!")
    else:
        print("❌ API key invalid or expired:", data.get("message"))
        print("🔁 Try getting a new key from @tgmusic_apibot")

except Exception as e:
    print("❌ Failed to connect to proxy:", str(e))
