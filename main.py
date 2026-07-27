from dotenv import load_dotenv
import os
import requests
import sqlite3

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
SERIES= [
    {
        "code": "UNRATE",
        "name": "Unemployment Rate",
        "unit": "Percent"
    },
    {
        "code": "CPIAUCSL",
        "name": "Consumer Price Index",
        "unit": "Index 1982-1984=100"
    },
    {
        "code": "FEDFUNDS",
        "name": "Federal Funds Rate",
        "unit": "Percent"
    }
]



def main():
    load_dotenv()

    api_key = os.getenv("FRED_API_KEY")

    if not api_key:
        print("Error: FRED_API_KEY not found. Please check your .env file")
        return

    for series in SERIES:
        params = {
            "api_key": api_key,
            "series_id": series["code"],
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

        cursor.execute('''
        INSERT OR IGNORE INTO economic_series (series_code, series_name, unit)
        VALUES (?, ?, ?);
        ''', (
            series["code"],
            series["name"],
            series["unit"]
        ))

        cursor.execute("""
        SELECT id
        FROM economic_series
        WHERE series_code = ?;
        """, (series["code"],))

        print(cursor.fetchall())

        for obs in observations:
            date = obs['date']
            value = obs['value']

            if value == '.':
                value = None
            else:
                value = float(value)

            cursor.execute("""
            INSERT OR IGNORE INTO economic_observations (series_id, date, value)
            VALUES (?, ?, ?);
            """, (series_id, date, value))

        connection.commit()
        connection.close()


if __name__ == "__main__":
    main()

