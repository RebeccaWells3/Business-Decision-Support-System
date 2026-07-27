from dotenv import load_dotenv
import os
from database import initialize_database
from api_client import get_series_observations
from analysis import analyze_data, calculate_inflation_rate, interpret_economic_conditions

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
        observations = get_series_observations(api_key, series["code"])

        connection, cursor = initialize_database()

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

        series_id = cursor.fetchone()[0]

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

    results = analyze_data()

    latest_values = {}

    for code, name, date, value in results:
        latest_values[code] = value

    inflation_rate = calculate_inflation_rate()

    overall_outlook, interpretations = interpret_economic_conditions(
        inflation_rate,
        latest_values["UNRATE"],
        latest_values["FEDFUNDS"]
    )

    print("\nCurrent Economic Conditions")
    print("-" * 30)

    for code, name, date, value in results:
        print(f"{name}: {value} ({date})")

    print(f"Year-over-Year Inflation Rate: {inflation_rate:.2f}%")

    print("\nBusiness Outlook")
    print("------------------------------")
    print(overall_outlook)

    print("\nKey Factors")
    print("------------------------------")

    for interpretation in interpretations:
        print(f"- {interpretation}")

if __name__ == "__main__":
    main()

