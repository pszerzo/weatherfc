import requests
import os


def get_data(place, fc_days):
    api_key = os.getenv("WEATHERAPI")
    fc_days *= 8
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={fc_days}&appid={api_key}"
    data = requests.get(url).json()
    fc_data = data["list"][:fc_days]
    return fc_data


if __name__ == "__main__":
    print(get_data("Sydney", 4))