import sqlite3
import time

DB_NAME = "monitor.db"


# ==========================================
# CREATE DATABASE
# ==========================================

def init_db():

    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS metrics (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            cpu REAL,

            memory REAL,

            disk REAL
        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully!")


# ==========================================
# SAVE DATA
# ==========================================

def save_metrics(data):

    connection = sqlite3.connect(DB_NAME)

    connection.execute(
        """
        INSERT INTO metrics
        (timestamp, cpu, memory, disk)

        VALUES (?, ?, ?, ?)
        """,

        (
            data["timestamp"],
            data["cpu"],
            data["memory"],
            data["disk"]
        )
    )

    connection.commit()
    connection.close()

    print("Metrics saved successfully!")


# ==========================================
# GET HISTORY
# ==========================================

def get_history():

    connection = sqlite3.connect(DB_NAME)

    rows = connection.execute(
        """
        SELECT timestamp, cpu, memory, disk

        FROM metrics

        ORDER BY id DESC

        LIMIT 20
        """
    ).fetchall()

    connection.close()

    return rows


# ==========================================
# TEST DATABASE
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print("       DATABASE TEST")
    print("=" * 50)

    # Create database
    init_db()

    # Sample monitoring data
    sample_data = {

        "timestamp":
        time.strftime("%Y-%m-%d %H:%M:%S"),

        "cpu": 45.5,

        "memory": 60.2,

        "disk": 50.8
    }

    # Save sample data
    save_metrics(sample_data)

    # Get saved data
    history = get_history()

    print("\nDATABASE HISTORY")
    print("-" * 50)

    for row in history:

        print(
            "Time:", row[0],
            "| CPU:", row[1],
            "| Memory:", row[2],
            "| Disk:", row[3]
        )

    print("=" * 50)
    print("Database test completed!")