# შექმენით User და Profile ცხრილი, დაამატეთ 5 ჩანაწერი თითოეულისთვის. 
# დაწერეთ ერთ ვერსია mysql.connector-ის გამოყენებით:

# User ცხრილი:
# 	id (Primary Key, Integer, Auto-increment)
# 	username (String, Unique, Not Null)
# 	email (String, Unique, Not Null)

# Profile ცხრილი:
# 	id Primary Key
# 	user_id მეორადი გასაღები მომხარებლების ცხრილზე ((Foreign Key to User's id)
# 	bio String
# 	profile_picture String

# დაიმახსოვრეთ უნდა გქონდეთ one-to-one relationship

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123asdASD",
    database="it_step_db"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    bio TEXT,
    profile_picture VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(id)
)
""")

conn.commit()

cursor.close()

cursor = conn.cursor()

user_data = [
    ("Daviti", "daviti@gmail.com"),
    ("Giorgi", "giorgi@gmail.com"),
    ("Armazi", "armazi@gmail.com"),
    ("Vano", "vano@gmail.com"),
    ("Beqa", "beqa@gmail.com")
]

insert_user_query = "INSERT INTO User (username, email) VALUES (%s, %s)"
cursor.executemany(insert_user_query, user_data)
conn.commit()

profile_data = [
    (1, "Bio for Daviti", "daviti.jpg"),
    (2, "Bio for Giorgi", "giorgi.jpg"),
    (3, "Bio for Armazi", "armazi.jpg"),
    (4, "Bio for Vano", "vano.jpg"),
    (5, "Bio for Beqa", "beqa.jpg")
]

insert_profile_query = "INSERT INTO Profile (user_id, bio, profile_picture) VALUES (%s, %s, %s)"
cursor.executemany(insert_profile_query, profile_data)
conn.commit()

cursor.close()
conn.close()