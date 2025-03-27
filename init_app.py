'''
    Filename: init_app.py
    Description: Initialization script to run once at application startup
'''

import os
import sqlite3

def init_app():
    print("Initializing application...")
    
    # Get base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set up directories
    logs_folder = os.path.join(base_dir, "user_logs")
    uploads_folder = os.path.join(base_dir, "static", "uploads")
    
    # Create directories if they don't exist
    for folder in [logs_folder, uploads_folder]:
        if not os.path.exists(folder):
            print(f"Creating directory: {folder}")
            os.makedirs(folder)
    
    # Set up database
    db_path = os.path.join(base_dir, "users.db")
    print(f"Setting up database at: {db_path}")
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create tables
    print("Creating database tables...")
    
    # Create users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        gmail TEXT UNIQUE NOT NULL
    )
    ''')
    
    # Create history table
    c.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        image TEXT NOT NULL,
        text TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create user_sessions table
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        session_id TEXT NOT NULL,
        ip_address TEXT,
        device_info TEXT,
        last_active DATETIME
    )
    ''')
    
    # Create user_preferences table
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_preferences (
        user_id INTEGER PRIMARY KEY,
        analytics INTEGER DEFAULT 0,
        notifications INTEGER DEFAULT 0,
        language TEXT DEFAULT 'en'
    )
    ''')
    
    # Create user_2fa table
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_2fa (
        user_id INTEGER PRIMARY KEY,
        enabled INTEGER DEFAULT 0,
        secret TEXT
    )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Application initialization complete!")

if __name__ == "__main__":
    init_app() 