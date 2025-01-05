import requests
import os


def get_data(place, fc_days, kind):
    api_key = os.getenv("WEATHERAPI")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={fc_days}&appid={api_key}"
    data = requests.get(url).json()
    fc_data = data["list"][:fc_days]

    if kind == "Temperature":
        result = [days["main"]["temp_kf"] for days in fc_data]
    elif kind == "Sky":
        result = [days["weather"][0]["description"] for days in fc_data]
    return result

if __name__ == "__main__":
    print(get_data("Sydney", 4, "Temperature"))