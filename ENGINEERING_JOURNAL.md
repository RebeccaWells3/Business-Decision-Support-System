# Engineering Journal

## Entry 1 – Project Planning
**Date:** July 16, 2026

### Objective

When I started planning this capstone, my main goal was to build a project that would strengthen my portfolio, build on the skills I developed throughout the summer, and challenge me to learn something new. I honestly wasn't sure what kind of project would be the best choice or where to start.

During the planning process, I learned that starting with the business problem instead of the technology—and defining the functional requirements before writing any code—made it much easier to make decisions about the project. By the end of the planning session, I had a much clearer direction for what I wanted to build.

### Decisions Made

1. As I planned my capstone, I wanted to choose a project that would build on what I learned throughout the summer while also giving me the opportunity to learn something new and strengthen my portfolio.


2. I decided to define the functional requirements before writing any code. One of the biggest differences from my previous projects was starting with a plan instead of immediately writing code, and I liked having that clear direction before I began building the application.

### Why I Made These Decisions

I wanted this project to build on the skills I developed throughout the summer because I knew I couldn't continue strengthening those skills without using them. At the same time, I wanted the project to challenge me to learn something new instead of only repeating what I already knew.

I also wanted to build a strong technical foundation that would prepare me for future internships and jobs while making me a stronger candidate. I knew that building projects that combined multiple technologies would give me more experience applying my technical skills and strengthen the foundation I need to continue learning more advanced technologies in the future.

During the planning process, I also learned that defining the functional requirements before writing any code gave me a much clearer understanding of what I needed to build. Having a plan before I started coding made it easier to organize the project and make decisions throughout the development process.

### Alternatives Considered

During the planning process, I explored whether the project should use current or historical economic data. Since my goal was to build a project that would strengthen my portfolio and support real-world business decision making, I decided to use current economic data.

I also explored whether to present the analysis through a command-line application or a web application. I decided to build a web application because it would create a better user experience and provide an opportunity to learn a new framework while building a more realistic application.

### Challenges

The biggest challenge during the planning process was deciding what kind of project to build. I wasn't sure which business problem would be the best fit or which project would best demonstrate the skills I developed throughout the summer. I wanted to choose a project that would challenge me, build on what I had already learned, and clearly demonstrate my technical abilities.

### Lessons Learned

The biggest lesson I learned during the planning process was the value of defining the functional requirements before writing any code. Taking the time to identify what the application needed to do gave me a much clearer understanding of the overall direction of the project before I started building it.

### Next Steps

- Finalize the application design.
- Begin implementing the application one feature at a time.
- Continue documenting decisions and lessons throughout development.

# Entry 2 - API Analysis and Data Transformation Design
**Date:** July 20, 2026

## Objective

Continue designing the application by analyzing the FRED API response and defining how the application should handle the data before storing it.

## Decisions Made

- Store only the `date` and `value` fields from each observation.
- Exclude the `realtime_start` and `realtime_end` metadata fields.
- Convert numeric values from strings to `float` during transformation.
- Convert `"."` values to Python `None`, which SQLite stores as `NULL`.
- Treat the `date` field as required.
- Reject individual observations that are missing a `date`.
- Stop the pipeline and notify the user if no observations are returned.

## Why I Made These Decisions

I wanted the application to store only the data needed to answer the business question while avoiding unnecessary information from the API response. I also wanted the application to handle missing or invalid data in a consistent way so that the database would contain reliable information for later analysis. As I evaluated different approaches, I chose the options that kept the application simpler while still meeting the project's requirements.

## Alternatives Considered

- Storing all fields returned by the FRED API instead of only the fields needed for analysis.
- Keeping numeric values as strings instead of converting them before storage.
- Converting `"."` to `0` instead of storing it as `NULL`.
- Skipping observations with missing values instead of storing them.
- Keeping observations without a `date` instead of rejecting them.
- Continuing the pipeline when no observations are returned instead of stopping and notifying the user.

## Challenges

This session required me to make engineering and data design decisions before writing code, which was different from my previous projects. I've found that I usually understand new concepts better after implementing them, so I adjusted my approach to focus on learning the reasoning as I build the application.

## Lessons Learned

No major technical lessons yet. This session focused on planning the application's data handling and design decisions before implementation.

## Next Steps

- Set up API key security using `.env` and `.gitignore`.
- Finalize the application's initial project structure.
- Implement the FRED API retrieval function.
- Begin building the data pipeline (retrieve → validate → transform → store).

## Entry 3 – FRED API Integration
**Date:** July 20, 2026

### Objective

My main goal was to securely set up the FRED API key and retrieve unemployment data for the project. I also wanted to understand how the API returned the data so I would know what information to store in the database.

### Decisions Made

1. I decided to include a `.env.example` file so the project could be shared without exposing the actual FRED API key. This also gives anyone using the project a template for setting up their own API key.

2. I decided to use constants for values like the API URL and series ID because they are used throughout the program and can be updated in one place if they ever need to change.

3. I decided to store only the `date` and `value` fields from the API response because those are the only pieces of information the project needs for analysis and storing the data in the database.

### Why

I wanted to build this part of the project with future changes in mind instead of just making it work. Keeping the API key secure, using constants for values that could change, and only storing the data the project actually needs will make the project easier to maintain as I continue building it.

### Alternatives Considered

I could have hardcoded the API key into the project or stored all of the data returned by the API. Instead, I chose to keep the API key secure using a `.env` file and only plan to store the data the project actually needs for analysis.

### Challenges

There weren't any major technical challenges during this session. The biggest challenge was keeping track of all of the new information as I worked through each step of retrieving and understanding the API data.

### Lessons Learned

I learned that larger projects involve a lot more planning and design decisions than the smaller projects I've worked on before. Taking the time to think through those decisions before writing more code should make the rest of the project easier.

### Next Steps

- Extract the `date` and `value` fields from each observation in the API response.

- Store the data in a SQLite database.

- Verify that the records were stored correctly before beginning the data analysis portion of the project.

# Entry 4- Refactoring the Project and Building the Analysis Layer
**Date:** July 21 & 27

### Objective

The goal of these sessions was to improve the structure of the project before continuing to add new features. I wanted to organize the code into separate modules so each file had a clear responsibility. After that, I began building the analysis portion of the project by querying the stored economic data and calculating a year-over-year inflation rate.

### Decisions Made

1. I moved the database initialization code into a separate `database.py` module instead of keeping everything in `main.py`.

2. I created an `api_client.py` module to handle communication with the FRED API. This removed the API request logic from `main.py` and made the program easier to organize.

3. I created an `analysis.py` module to keep the SQL queries and business calculations separate from the rest of the application.

4. I decided to calculate the year-over-year inflation rate instead of only displaying the latest CPI value because the inflation rate provides more meaningful business information than the raw CPI index.

### Why I Made These Decisions

As the project grew, keeping everything in one file was becoming difficult to manage. Separating the database, API, and analysis logic into different modules made the project easier to understand and maintain.

Calculating inflation instead of simply displaying the CPI value also made the application better at answering the original business question. A business user can understand an inflation percentage much more easily than a CPI index value by itself.

### Challenges

One of the biggest challenges during these sessions was understanding how data moved between modules. Passing values into functions and returning results took some time to fully understand.

I also ran into a bug when retrieving a database ID because `fetchone()` returned a tuple instead of a single value. After I realized what was happening, indexing into the tuple fixed the problem.

Another challenge was learning several new engineering concepts at the same time. We decided to stay focused on completing the project's MVP first and return to the deeper engineering discussions after the project was finished.

### Lessons Learned

- Refactoring changes the structure of a program without changing its behavior.
- Separating responsibilities into different modules makes a project easier to organize and maintain.
- Database query results are not always returned in the format I expect, so I need to understand what a query returns before using it.
- Business applications often need calculations that transform raw data into information that is meaningful to users.

### Next Steps

- Interpret the economic indicators instead of only displaying their values.
- Improve the business-focused output.
- Complete the remaining MVP features and documentation.
- Review the project's engineering decisions so I can confidently explain them during interviews.

## Entry 5 – Completing the Business Decision Support System

**Date:** July 27, 2026

### Objective

My goal for this session was to complete the remaining features of the Business Decision Support System, review the project's documentation, and prepare it for my portfolio. I wanted to make sure the application accurately answered the original business question and that the repository was organized and documented in a professional way.

### Decisions Made

- I added a business interpretation layer that analyzes the economic indicators and generates an overall business outlook.
- I updated the project requirements so they accurately reflected the completed application instead of the original plan.
- I created a comprehensive README that explains the project's purpose, technologies, workflow, installation, and key skills demonstrated.

### Why

One of the biggest lessons from this project was that writing the code is only part of building software. Good documentation helps other developers, employers, and even my future self understand what the application does, how it works, and why certain engineering decisions were made.

I also wanted the finished project to accurately represent what I built. Updating the requirements and documentation helped ensure that everything in the repository matched the final implementation.

### Challenges

The biggest challenge during the final phase wasn't writing additional code. Instead, it was deciding where to stop. There were several features that could have been added, such as a Flask web interface or data visualizations, but continuing to add features would have delayed completing the project.

### Lessons Learned

This project showed me the importance of defining a solid scope and finishing a complete application before adding additional features. I also learned that software engineering includes much more than programming. Planning, documentation, version control, testing, and explaining design decisions are all important parts of building professional software.

Looking back over the summer, I also realized how much this project brought together skills from my previous projects while introducing me to a more complete software engineering process.

### Next Steps

The implementation phase of the project is complete. My next step is to review the engineering decisions behind the project and practice explaining the system, architecture, and design choices so I can confidently discuss them during internship and job interviews.


