# Weather Data Integrator

## Overview
This project is a technical implementation of a real-time weather data retrieval system. Developed as part of my **NCC Level 3 Diploma in Computing** portfolio, it demonstrates in handling external APIs, parsing JSON data, and implementing error-handling logic in Python.

The application interfaces with the OpenWeatherMap API to fetch, process, and display localized meteorological data based on user input.

## Key Technical Features

* **REST API Integration:** Implements GET requests to retrieve live data from the OpenWeatherMap endpoint.
* **JSON Data Parsing:** Efficiently navigates complex nested dictionaries to extract specific values (Temperature, Humidity, Wind Speed).
* **Input Validation:** Handles potential errors such as invalid city names or network connectivity issues.
* **Modular Design:** Code is structured for readability and future expansion (e.g., adding a GUI or Database logging).


## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `requests` (HTTP library), `json` (Data handling)
* **Source:** OpenWeatherMap API (You can use your preferable API)

## Implementation Details
To ensure security, the API Key is managed via environment variables (or a config file) to prevent unauthorized usage.

## Set up and Installation
1. Prerequisites
    Before running the script, install the required library:
    ```bash
    pip install requests
    pip install requests python-dotenv

2. Get an API Key
    To run this project, you must obtain your own API key:
    Sign up for a free account at OpenWeatherMap.
    Generate an API key from your dashboard.

3. Configuration 

    Configuration
    Create a file named .env in the root directory.
    Add your key to the file:
        OPENWEATHER_API_KEY=your_actual_key_here

4. Usage
    Clone the repository.
    Ensure your .env file is set up.
    Run the script:
    ```bash
    python_weather_api.py
    

📜 License

MIT License
Copyright (c) 2025 Sai Thuta
Permission is hereby granted, free of charge, to any person obtaining a copy...

🙌 Acknowledgements

• Based on concepts from "Python For Everybody" (University of Michigan, Coursera)
• Retrieving data by using API and handling JSON data fromat
• Credit to Dr. Charles Severance for the original concepts
• Project refactored and implemented by Sai Thuta Hlaing (Cairney)


