
#!/usr/bin/env python3
import requests
import mysql.connector
from datetime import datetime
import os

API_KEY = ("07af4f5ddcb0378dc9ca3f3549a1279e")  # safer than hardcoding
CITY = "Helsinki"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='exampleuser',
    password='Yup#2025',
    database='weather_db'
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    description VARCHAR(100),
    timestamp DATETIME
)
''')

# Fetch data
response = requests.get(URL)
data = response.json()
 
temp = data['main']['temp']
desc = data['weather'][0]['description']
timestamp = datetime.now()

# Insert data
cursor.execute(
    'INSERT INTO weather_data (city, temperature, description, timestamp) VALUES (%s, %s, %s, %s)',
    (CITY, temp, desc, timestamp)
)
conn.commit()
cursor.close()
conn.close()

print(f"Data saved: {CITY} {temp}°C {desc}")


