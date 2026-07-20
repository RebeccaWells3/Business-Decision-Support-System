from dotenv import load_dotenv
import os
import requests
import json

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

    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()

