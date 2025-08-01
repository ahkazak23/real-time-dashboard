import requests

def get_coordinates(city: str = "Istanbul") -> tuple[float, float]:
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Geocoding error: {response.status_code}")
    results = response.json().get("results")
    if not results:
        raise ValueError(f"City not found: {city}")
    loc = results[0]
    return loc["latitude"], loc["longitude"]

def get_weather(latitude: float = 41.01, longitude: float = 28.97) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,weathercode,wind_speed_10m"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Weather API error: {response.status_code}")
    return response.json()

def get_air_quality(latitude: float = 41.01, longitude: float = 28.97) -> dict:
    url = (
        "https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={latitude}&longitude={longitude}"
        "&hourly=pm10,pm2_5,carbon_monoxide"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"AQI API error: {response.status_code}")
    return response.json()

if __name__ == "__main__":
    print("Weather:", get_weather())
    print("Air Quality:", get_air_quality())
