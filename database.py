import sqlite3

def initialize_database():
    connection = sqlite3.connect('business_decision_support.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS economic_series(
        id INTEGER PRIMARY KEY,
        series_code TEXT UNIQUE NOT NULL,
        series_name TEXT NOT NULL,
        unit TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS economic_observations(
        id INTEGER PRIMARY KEY,
        series_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        value REAL,
        FOREIGN KEY(series_id) REFERENCES economic_series(id),
        UNIQUE(series_id,date)
    );
    ''')

    return connection,cursor