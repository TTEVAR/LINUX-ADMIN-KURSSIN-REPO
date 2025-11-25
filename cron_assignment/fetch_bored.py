#!/usr/bin/env python3
import mysql.connector
from datetime import datetime
import random

# List of dummy activities
activities = [
    "Read a book",
    "Go for a walk",
    "Learn Python",
    "Do a puzzle",
    "Listen to music",
    "Meditate for 10 minutes",
    "Write a journal entry",
    "Draw or paint something",
    "Try a new recipe",
    "Organize your desk"
]

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="exampleuser",
    password="Yup#2025",
    database="exampledb"
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS bored_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    activity TEXT,
    type VARCHAR(50),
    participants INT,
    timestamp DATETIME
)
''')

# Pick a random activity
activity = random.choice(activities)

# Insert into table
cursor.execute(
    "INSERT INTO bored_data (activity, type, participants, timestamp) VALUES (%s, %s, %s, %s)",
    (activity, "fun", 1, datetime.now())
)
conn.commit()
cursor.close()
conn.close()

print(f"Inserted dummy activity: {activity}")
