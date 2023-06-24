import requests
import json
import matplotlib.pyplot as plt

def get_weather(city):
    api_key = "41538b3bc8f99dd331c9251ec38b04f4"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/onecall"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change units to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data


def parse_weather_data(data):
    if data["cod"] != 200:
        raise Exception(f"Error: {data['message']}")

    main_info = data["current"]["weather"][0]["main"]
    description = data["current"]["weather"][0]["description"]
    temperature = data["current"]["temp"]
    humidity = data["current"]["humidity"]

    hourly_temperatures = [hour_data["temp"] for hour_data in data["hourly"][:24]]

    return main_info, description, temperature, humidity, hourly_temperatures


def main():
    city = input("Enter a city name: ")
    try:
        print("Fetching weather data...")
        weather_data = get_weather(city)
        print("Weather data fetched successfully!")

        main_info, description, temperature, humidity, hourly_temperatures = parse_weather_data(weather_data)

        print(f"Weather in {city}:")
        print(f"Condition: {main_info} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")

        # Plotting the temperature chart
        plt.plot(hourly_temperatures, color='orange')
        plt.title(f"Temperature Forecast for {city}")
        plt.xlabel("Time (hours)")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
