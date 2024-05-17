import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    city = city_entry.get()
    if city:
        API_KEY = 'Replace with your actual API key'
        BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            weather_report = data['weather'][0]['description']

            result = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa\nWeather Report: {weather_report}"
            weather_label.config(text=result)
        else:
            messagebox.showerror("Error", "City Not Found")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")


# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create widgets
city_label = tk.Label(root, text="Enter City Name:")
city_label.grid(row=0, column=0, padx=10, pady=5)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 14), justify='left')
weather_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
