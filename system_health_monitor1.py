import psutil
import datetime

def system_health_check():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nSystem Health Report - {timestamp}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")

    if cpu_usage > 80:
        print("⚠️  Alert: High CPU usage!")
    if memory.percent > 80:
        print("⚠️  Alert: High Memory usage!")
    if disk.percent > 80:
        print("⚠️  Alert: Low Disk Space!")

if __name__ == "__main__":
    system_health_check()