import sqlite3

conn = sqlite3.connect("history.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scan_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    prediction TEXT,

    confidence REAL,

    trust_score INTEGER,

    bot_probability INTEGER,

    scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

conn.close()

print("Database Created Successfully")