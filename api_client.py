import requests

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

def get_series_observations(api_key,series_code):
    params = {
        "api_key": api_key,
        "series_id": series_code,
        "file_type": "json"
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    observations = data["observations"]

    return observations
