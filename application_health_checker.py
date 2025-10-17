import requests
from datetime import datetime

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Application is up and running normally. ({response.status_code})")
        else:
            print(f"⚠️ Application responded but with unexpected status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Server may be slow or down.")
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Server is unreachable.")
    except Exception as e:
        print(f"⚠️ Unexpected error occurred: {e}")
    finally:
        print(f"🕒 Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 🔹 Run this part — make sure to replace with your actual OrangeHRM URL
if __name__ == "__main__":
    url = "https://opensource-demo.orangehrmlive.com/"
    check_application_health(url)
