# Business Decision Support System

## Project Overview

The Business Decision Support System is a Python application that retrieves current U.S. economic data from the Federal Reserve Economic Data (FRED) API, stores it in a SQLite database, analyzes key economic indicators, and generates business insights to support decision-making. The goal of the project is to help Business Analysts quickly evaluate current economic conditions without manually gathering data from multiple sources.

The application focuses on three economic indicators:

- Inflation
- Unemployment
- Federal Funds Rate

Using these indicators, the system calculates the current inflation rate, evaluates overall economic conditions, and provides a business outlook along with explanations of the key factors influencing that outlook.

**Project Status:** Complete

## Technologies Used

- Python
- SQLite
- SQL
- REST APIs
- FRED API
- Requests
- python-dotenv
- Git
- GitHub

## Skills Demonstrated


- REST API integration
- JSON validation and transformation
- Relational database design with SQLite
- SQL querying
- Modular Python application design
- Business logic implementation
- Version control using Git and GitHub
- Requirements documentation and software planning

## Features

- Retrieves current economic data from the FRED API
- Validates and transforms API responses
- Stores economic data in a SQLite relational database
- Calculates the current year-over-year inflation rate
- Retrieves the latest unemployment and federal funds rate data
- Generates a business outlook based on current economic conditions
- Provides explanations of the economic factors influencing the business outlook

## System Workflow

1. Retrieve economic data from the FRED API.
2. Validate the retrieved data.
3. Transform the data into a consistent format.
4. Store the data in a SQLite database.
5. Query and analyze the stored data.
6. Calculate the year-over-year inflation rate.
7. Generate a business outlook based on current economic conditions.
8. Display the analysis results to the user.

## Installation

1. Clone the repository.

```bash
git clone https://github.com/RebeccaWells3/Business-Decision-Support-System.git
```

2. Navigate to the project directory.

```bash
cd Business-Decision-Support-System
```

3. Create a virtual environment.

```bash
python3 -m venv .venv
```

4. Activate the virtual environment.

```bash
source .venv/bin/activate
```

5. Install the required packages.

```bash
pip install -r requirements.txt
```

```text
FRED_API_KEY=your_api_key_here
```

6. Create a `.env` file in the project root and add your FRED API key.

```text
FRED_API_KEY=your_api_key_here
```

7. Run the application.

```bash
python main.py
```

## Sample Output

```text
Current Economic Conditions
------------------------------
Consumer Price Index: 332.568 (2026-06-01)
Federal Funds Rate: 3.63 (2026-06-01)
Unemployment Rate: 4.2 (2026-06-01)
Year-over-Year Inflation Rate: 3.73%

Business Outlook
------------------------------
Business conditions appear stable.

Key Factors
------------------------------
- Moderate inflation may gradually increase business costs.
- Moderate interest rates may moderately affect borrowing costs.
- Moderate unemployment suggests a balanced labor market.
```

## Project Structure

```text
Business-Decision-Support-System/
│
├── analysis.py                # Business analysis and interpretation
├── api_client.py              # Retrieves data from the FRED API
├── database.py                # Database creation and data storage
├── main.py                    # Application entry point
├── requirements.txt           # Project dependencies
├── REQUIREMENTS.md            # Functional requirements
├── ENGINEERING_JOURNAL.md     # Development decisions and reflections
├── README.md                  # Project documentation
├── .gitignore                 # Excludes sensitive and unnecessary files
└── .env.example               # Example environment variable configuration
```

## What I Learned

Building this project allowed me to bring together many of the software engineering concepts I had learned throughout the summer into one complete application. It also introduced me to several new concepts, including documenting requirements before implementation, organizing a larger modular application, and generating business insights from economic data.

Throughout the project, I gained experience with:

- Retrieving data from a REST API
- Validating and transforming JSON data
- Designing and querying a relational database with SQLite
- Organizing a Python project into reusable modules
- Separating data retrieval, storage, analysis, and presentation into different components
- Using Git through PyCharm and GitHub to track development throughout the project
- Documenting software requirements and engineering decisions before and during implementation

## Future Enhancements

Possible future improvements include:

- Develop a web interface using Flask.
- Compare current economic conditions with historical trends.
- Visualize economic trends with charts and graphs.
- Analyze additional economic indicators from the FRED API.
- Allow users to customize the indicators included in the analysis.

## Documentation

Additional project documentation is included in the repository:

- `REQUIREMENTS.md` – Functional requirements and project planning
- `ENGINEERING_JOURNAL.md` – Engineering decisions, challenges, and lessons learned
