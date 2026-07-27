import sqlite3

def analyze_data():
    connection = sqlite3.connect("business_decision_support.db")
    cursor = connection.cursor()

    cursor.execute("""
            SELECT
                economic_series.series_code,
                economic_series.series_name,
                economic_observations.date,
                economic_observations.value
            FROM economic_series
            JOIN economic_observations
                ON economic_series.id = economic_observations.series_id
            WHERE economic_observations.value IS NOT NULL
              AND economic_observations.date = (
                  SELECT MAX(latest.date)
                  FROM economic_observations AS latest
                  WHERE latest.series_id = economic_series.id
                    AND latest.value IS NOT NULL
              )
            ORDER BY economic_series.series_code;
        """)

    results = cursor.fetchall()

    connection.close()

    return results

def calculate_inflation_rate():
    connection = sqlite3.connect("business_decision_support.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT date, value
        FROM economic_observations
        WHERE series_id = (
            SELECT id
            FROM economic_series
            WHERE series_code = 'CPIAUCSL'
        )
        AND value IS NOT NULL
        ORDER BY date DESC
        LIMIT 13;
    """)

    results = cursor.fetchall()

    connection.close()

    current_cpi = results[0][1]
    previous_cpi = results[12][1]

    inflation_rate = ((current_cpi - previous_cpi) / previous_cpi) * 100

    return inflation_rate

