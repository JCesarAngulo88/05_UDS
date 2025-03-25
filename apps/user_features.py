"""
This module is not used, take it as a reference to user_db.py
"""
import sqlite3
import bcrypt

# Database setup
def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create a table to store user credentials
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password BLOB NOT NULL,
            project TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a new user to the database
def register_user(username, password, project):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert into the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, hashed_password, project)
            VALUES (?, ?, ?)
        ''', (username, hashed_password, project))
        conn.commit()
        print(f"User '{username}' registered successfully!")
    except sqlite3.IntegrityError:
        print(f"Username '{username}' already exists.")
    finally:
        conn.close()

# User login
def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ").encode('utf-8')  # Encode password to bytes
    project = input("Enter your project: ")

    # Fetch user details from the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT hashed_password, project FROM users WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hashed_password, stored_project = result
        # Verify the password and project
        if bcrypt.checkpw(password, stored_hashed_password) and stored_project == project:
            print("Login successful! Access granted to the app.")
            return True
        else:
            print("Invalid password or project. Access denied.")
            return False
    else:
        print("Username not found. Access denied.")
        return False
