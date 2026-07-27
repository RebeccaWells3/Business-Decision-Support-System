from dotenv import load_dotenv
import os
import requests
import sqlite3

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
SERIES_ID = "UNRATE"


def main():
    load_dotenv()

    api_key = os.getenv("FRED_API_KEY")

    if not api_key:
        print("Error: FRED_API_KEY not found. Please check your .env file")
        return

    params = {
        "api_key": api_key,
        "series_id": SERIES_ID,
        "file_type": "json"
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    observations = data["observations"]

    connection = sqlite3.connect('business_decision_support.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS economic_series(
        id INTEGER PRIMARY KEY,
        series_code TEXT,
        series_name TEXT,
        unit TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS economic_observations(
        id INTEGER PRIMARY KEY,
        series_id INTEGER,
        date TEXT,
        value REAL,
        FOREIGN KEY(series_id) REFERENCES economic_series(id)
    );
    ''')

    cursor.execute('''
    INSERT INTO economic_series (series_code, series_name, unit)
    VALUES ('UNRATE', 'Unemployment Rate', 'Percent');
    ''')

    cursor.execute("""
    SELECT id
    FROM economic_series
    WHERE series_code = ?;
    """, (SERIES_ID,))

    series_id = cursor.fetchone()[0]

    for obs in observations:
        date = obs['date']
        value = obs['value']

        if value == '.':
            value = None
        else:
            value = float(value)

        cursor.execute("""
        INSERT INTO economic_observations (series_id, date, value)
        VALUES (?, ?, ?);
        """, (series_id, date, value))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()

