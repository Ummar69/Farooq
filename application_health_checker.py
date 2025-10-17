import requests
from datetime import datetime

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        if status_code == 200:
            print(f"✅ {url} is UP and responding normally.")
        else:
            print(f"⚠️ {url} returned status code {status_code}.")
    except requests.ConnectionError:
        print(f"❌ {url} is DOWN (connection failed).")
    except requests.Timeout:
        print(f"⏱️ {url} is DOWN (request timed out).")
    except Exception as e:
        print(f"⚠️ Unexpected error occurred: {e}")
    finally:
        print(f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "_main_":
    website_url = "https://www.google.com"
    check_application_health(website_url)
    website_url = "https://www.google.com"
    check_application_health(website_url)