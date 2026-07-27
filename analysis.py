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

def interpret_economic_conditions(inflation_rate, unemployment_rate, federal_funds_rate):
    interpretations = []

    overall_outlook = ""

    if inflation_rate >= 4:
        interpretations.append("High inflation may increase business costs.")
    elif inflation_rate >= 2:
        interpretations.append("Moderate inflation may gradually increase business costs.")
    else:
        interpretations.append("Low inflation suggests relatively stable prices.")

    if federal_funds_rate >= 5:
        interpretations.append("High interest rates may increase borrowing costs for businesses.")
    elif federal_funds_rate >= 2:
        interpretations.append("Moderate interest rates may moderately affect borrowing costs.")
    else:
        interpretations.append("Low interest rates may encourage business investment.")

    if unemployment_rate >= 6:
        interpretations.append("High unemployment may indicate weaker consumer demand.")
    elif unemployment_rate >= 4:
        interpretations.append("Moderate unemployment suggests a balanced labor market.")
    else:
        interpretations.append("Low unemployment may make hiring more competitive.")

    if inflation_rate >= 4 or federal_funds_rate >= 5:
        overall_outlook = "Business conditions appear challenging."
    elif inflation_rate >= 2 or federal_funds_rate >= 2 or unemployment_rate >= 4:
        overall_outlook = "Business conditions appear stable."
    else:
        overall_outlook = "Business conditions appear favorable."

    return overall_outlook, interpretations

