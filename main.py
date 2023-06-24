import argparse
import config
from weather.api import fetch_weather_data
from weather.parser import parse_weather_data
from weather.models import WeatherData
from weather.utils import display_weather_info

def main():
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Weather Forecasting Tool")
    parser.add_argument("city", help="City name for weather forecast")
    args = parser.parse_args()

    # Fetch weather data
    response = fetch_weather_data(args.city, config.API_KEY)
    if response.status_code == 200:
        weather_data = parse_weather_data(response.json())
        if weather_data:
            # Create WeatherData object
            weather_obj = WeatherData(args.city, weather_data)
            # Display weather information
            display_weather_info(weather_obj)
        else:
            print("Failed to parse weather data.")
    else:
        print(f"Failed to fetch weather data. Error: {response.status_code}")


if __name__ == "__main__":
    main()
