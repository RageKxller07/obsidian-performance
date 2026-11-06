import sqlite3
import random
from datetime import datetime, timedelta

DB_FILE = 'obsidian.db'

# Pre-defined mock athletes and disciplines
ATHLETES = ["Saurav D.", "Pritha S.", "Srushti H.", "Himanshu K.", "Priyanka M."]
DISCIPLINES = ["Sprint", "Endurance", "Strength"]
STRENGTH_EXERCISES = ["SQUAT", "BENCH PRESS", "DEADLIFT", "OVERHEAD PRESS", "BARBELL ROW"]

def generate_mock_data(total_records=200):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Ensure tables exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            athlete_name TEXT,
            activity_type TEXT,
            duration REAL,
            rpe REAL,
            avg_hr REAL,
            top_speed REAL,
            distance REAL,
            exercise_name TEXT,
            weight REAL,
            sets INTEGER,
            reps INTEGER,
            user_id INTEGER
        )
    ''')

    start_date = datetime.now() - timedelta(days=90)

    for i in range(total_records):
        # Generate progressive timestamps over the last 90 days
        session_time = start_date + timedelta(hours=i * (90 * 24 / total_records))
        timestamp_str = session_time.strftime("%Y-%m-%d %H:%M:%S")

        athlete = random.choice(ATHLETES)
        activity = random.choice(DISCIPLINES)
        rpe = round(random.uniform(6.0, 10.0), 1)
        avg_hr = round(random.uniform(130, 192), 0)
        
        duration = None
        top_speed = None
        distance = None
        exercise_name = None
        weight = None
        sets = None
        reps = None

        if activity == "Sprint":
            duration = round(random.uniform(20.0, 60.0), 1)
            top_speed = round(random.uniform(22.0, 32.5), 1)
        elif activity == "Endurance":
            duration = round(random.uniform(30.0, 120.0), 1)
            distance = round(random.uniform(5.0, 25.0), 2)
        elif activity == "Strength":
            exercise_name = random.choice(STRENGTH_EXERCISES)
            weight = round(random.uniform(60.0, 180.0), 1)
            sets = random.randint(3, 5)
            reps = random.randint(3, 12)

        cursor.execute('''
            INSERT INTO workouts (
                timestamp, athlete_name, activity_type, duration, rpe, avg_hr, 
                top_speed, distance, exercise_name, weight, sets, reps, user_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            timestamp_str, athlete, activity, duration, rpe, avg_hr, 
            top_speed, distance, exercise_name, weight, sets, reps, 1
        ))

    conn.commit()
    conn.close()
    print(f"✅ Successfully injected {total_records} mock training records into {DB_FILE}!")

if __name__ == "__main__":
    generate_mock_data(300) # Change this number to 500 or 1000 to push limits further!