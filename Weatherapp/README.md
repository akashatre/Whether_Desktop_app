# Weather App

A simple Weather App using Tkinter for the GUI and OpenWeatherMap API for fetching weather data.

## Features

- Get current weather information by entering a city name.
- Displays temperature, humidity, pressure, and weather description.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. Install the required packages. It is recommended to use a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Replace `'Replace with your actual API key'` in the `get_weather` function with your actual API key from OpenWeatherMap.

## Usage

1. Run the application:

    ```bash
    python weather_app.py
    ```

2. Enter a city name in the input field and click "Get Weather".

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- `tkinter` (comes pre-installed with standard Python distribution)

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.

