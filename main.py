import json
import sys
from dataclasses import dataclass
from urllib.parse import quote
from urllib.request import urlopen


@dataclass
class WeatherData:
    city: str
    temperature: int
    country: str


def load_cities(filename):
    cities = []

    with open(filename, encoding="utf-8") as file:
        for line in file:
            city = line.strip()
            if city and city not in cities:
                cities.append(city)

    return cities


def get_weather(city):
    url = f"https://wttr.in/{quote(city, safe='')}?format=j1"
    with urlopen(url, timeout=30) as response:
        data = json.load(response)

    temperature = int(data["current_condition"][0]["temp_C"])
    country = data["nearest_area"][0]["country"][0]["value"]
    return WeatherData(city, temperature, country)


def print_statistics(weather_list):
    temperatures_by_country = {}

    for weather in weather_list:
        if weather.country not in temperatures_by_country:
            temperatures_by_country[weather.country] = []

        temperatures_by_country[weather.country].append(weather.temperature)

    for country, temperatures in temperatures_by_country.items():
        count = len(temperatures)
        average = sum(temperatures) / count
        minimum = min(temperatures)
        maximum = max(temperatures)
        print(
            f"{country} - {count} cities, avg: {average:+.1f} °C, "
            f"min: {minimum:+d} °C, max: {maximum:+d} °C"
        )


def main():
    filename = "Cities.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    try:
        cities = load_cities(filename)
    except Exception as error:
        print(f"Не удалось прочитать файл: {error}")
        return

    if not cities:
        print("В файле нет городов.")
        return

    weather_list = []
    for city in cities:
        try:
            weather = get_weather(city)
        except Exception as error:
            print(f"Не удалось получить погоду для {city}: {error}")
            continue

        weather_list.append(weather)
        print(f"{weather.city}, {weather.country} {weather.temperature:+d} °C")

    if weather_list:
        print()
        print_statistics(weather_list)


if __name__ == "__main__":
    main()
