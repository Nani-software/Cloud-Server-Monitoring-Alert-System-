import os
import platform
import socket
import time
import shutil
import random


# ==========================================
# CLOUD SERVER MONITORING & ALERT SYSTEM
# ==========================================


def get_server_info():
    """
    Get basic server/system information.
    """

    hostname = socket.gethostname()
    operating_system = platform.system()
    operating_system_version = platform.version()

    return {
        "hostname": hostname,
        "os": operating_system,
        "os_version": operating_system_version
    }


# ==========================================
# DISK MONITORING
# ==========================================

def get_disk_info():

    total, used, free = shutil.disk_usage("/")

    total_gb = round(total / (1024 ** 3), 2)
    used_gb = round(used / (1024 ** 3), 2)
    free_gb = round(free / (1024 ** 3), 2)

    usage_percentage = round(
        (used / total) * 100,
        2
    )

    return {
        "total": total_gb,
        "used": used_gb,
        "free": free_gb,
        "usage": usage_percentage
    }


# ==========================================
# DEMO CPU MONITORING
# ==========================================

def get_cpu_usage():

    # Demo value
    cpu = random.randint(10, 95)

    return cpu


# ==========================================
# DEMO MEMORY MONITORING
# ==========================================

def get_memory_usage():

    # Demo value
    memory = random.randint(20, 90)

    return memory


# ==========================================
# ALERT SYSTEM
# ==========================================

def check_alerts(cpu, memory, disk):

    alerts = []

    # CPU alert
    if cpu >= 80:

        alerts.append(
            f"WARNING: High CPU usage - {cpu}%"
        )

    # Memory alert
    if memory >= 80:

        alerts.append(
            f"WARNING: High Memory usage - {memory}%"
        )

    # Disk alert
    if disk >= 90:

        alerts.append(
            f"WARNING: High Disk usage - {disk}%"
        )

    return alerts


# ==========================================
# DISPLAY DASHBOARD
# ==========================================

def display_dashboard():

    print("\n")
    print("=" * 60)
    print("       CLOUD SERVER MONITORING SYSTEM")
    print("=" * 60)

    # Server information

    server = get_server_info()

    print("\nSERVER INFORMATION")
    print("-" * 60)

    print(
        "Hostname       :",
        server["hostname"]
    )

    print(
        "Operating System:",
        server["os"]
    )

    print(
        "OS Version     :",
        server["os_version"]
    )


    # CPU

    cpu = get_cpu_usage()

    print("\nCPU MONITORING")
    print("-" * 60)

    print(
        "CPU Usage      :",
        str(cpu) + "%"
    )


    # Memory

    memory = get_memory_usage()

    print("\nMEMORY MONITORING")
    print("-" * 60)

    print(
        "Memory Usage   :",
        str(memory) + "%"
    )


    # Disk

    disk = get_disk_info()

    print("\nDISK MONITORING")
    print("-" * 60)

    print(
        "Total Disk     :",
        str(disk["total"]) + " GB"
    )

    print(
        "Used Disk      :",
        str(disk["used"]) + " GB"
    )

    print(
        "Free Disk      :",
        str(disk["free"]) + " GB"
    )

    print(
        "Disk Usage     :",
        str(disk["usage"]) + "%"
    )


    # Alerts

    alerts = check_alerts(
        cpu,
        memory,
        disk["usage"]
    )


    print("\nSERVER STATUS")
    print("-" * 60)


    if alerts:

        print("STATUS: WARNING")

        for alert in alerts:

            print("⚠️", alert)

    else:

        print("STATUS: HEALTHY")
        print("Server is operating normally.")


    print("\n")
    print("=" * 60)


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("\nStarting Cloud Server Monitoring System...")

    time.sleep(1)

    display_dashboard()


# Program starts here

if __name__ == "__main__":

    main()