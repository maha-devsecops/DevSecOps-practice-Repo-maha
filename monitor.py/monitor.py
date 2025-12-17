import requests
import time

print("--- Adapureddi Maha DevOps Monitoring Tool (V1.0) ---")

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.invalid-site-test.com"
]

def check_site_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"✅ {url} : Active and Running (Status: 200)"
        else:
            return f"⚠️ {url} : Problem found (Status: {response.status_code})"
    except requests.exceptions.RequestException:
        return f"❌ {url} : Connection Error/Offline"

# ప్రతి వెబ్‌సైట్‌ను చెక్ చేయడానికి లూప్ వాడదాం
for site in websites:
    status_message = check_site_status(site)
    print(status_message)
    time.sleep(1) # ప్రతి చెకింగ్ తర్వాత 1 సెకను ఆగుతుంది

print("--- Monitoring Complete. ---")
