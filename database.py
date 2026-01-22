import sqlite3

DB_Name = "uphrs.db"

def get_connection():
    return sqlite3.connect(DB_Name)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        dob TEXT,
        gender TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT,
        patient_id TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medical_records (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        diagnosis TEXT,
        visit_date TEXT,
        facility TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medications (
        med_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        drug_name TEXT,
        dosage TEXT,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consent (
        patient_id TEXT PRIMARY KEY,
        allowed INTEGER
    )
    """)

    conn.commit()
    conn.close()