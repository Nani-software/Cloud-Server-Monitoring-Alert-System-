import platform
import socket
import shutil
import os
import time


def get_system_info():

    hostname = socket.gethostname()

    operating_system = platform.system()

    os_version = platform.version()

    cpu_count = os.cpu_count()

    total, used, free = shutil.disk_usage("/")

    total_gb = round(total / (1024 ** 3), 2)
    used_gb = round(used / (1024 ** 3), 2)
    free_gb = round(free / (1024 ** 3), 2)

    disk_usage = round((used / total) * 100, 2)

    current_time = time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return {
        "hostname": hostname,
        "os": operating_system,
        "os_version": os_version,
        "cpu_count": cpu_count,
        "memory": "Not Available",
        "disk": disk_usage,
        "disk_used": used_gb,
        "disk_total": total_gb,
        "disk_free": free_gb,
        "timestamp": current_time
    }


def get_processes():
    return []


# ==========================================
# TEST OUTPUT
# ==========================================

if __name__ == "__main__":

    data = get_system_info()

    print("=" * 50)
    print("     CLOUD SERVER MONITORING")
    print("=" * 50)

    print("Hostname       :", data["hostname"])
    print("Operating System:", data["os"])
    print("OS Version     :", data["os_version"])
    print("CPU Cores      :", data["cpu_count"])
    print("Memory         :", data["memory"])
    print("Disk Usage     :", str(data["disk"]) + "%")
    print("Disk Used      :", str(data["disk_used"]) + " GB")
    print("Disk Free      :", str(data["disk_free"]) + " GB")
    print("Disk Total     :", str(data["disk_total"]) + " GB")
    print("Time           :", data["timestamp"])

    print("=" * 50)