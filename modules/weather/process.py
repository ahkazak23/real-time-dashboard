from .fetch import get_weather, get_air_quality

# Weather condition codes
WEATHER_CODE_MAP = {
    0: "☀️ Clear",
    1: "🌤️ Mainly Clear",
    2: "⛅ Partly Cloudy",
    3: "☁️ Overcast",
    45: "🌫️ Fog",
    48: "🌫️ Depositing Rime Fog",
    51: "🌦️ Light Drizzle",
    61: "🌧️ Light Rain",
    71: "❄️ Light Snow",
    80: "🌧️ Rain Showers",
    95: "⛈️ Thunderstorm",
    99: "🌩️ Hail Thunderstorm"
}

def format_weather_data(raw: dict) -> dict:
    current = raw.get("current", {})
    code = current.get("weathercode")
    return {
        "temperature": current.get("temperature_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "weather_code": code,
        "weather_desc": WEATHER_CODE_MAP.get(code, "❓ Unknown"),
        "time": current.get("time"),
    }

def get_aqi_level(pm: float | None) -> str:
    if pm is None:
        return "Unknown"
    if pm <= 12:
        return "🟢 Good"
    elif pm <= 35:
        return "🟡 Moderate"
    elif pm <= 55:
        return "🟠 Unhealthy (Sensitive)"
    elif pm <= 150:
        return "🔴 Unhealthy"
    else:
        return "🟣 Very Unhealthy"

def format_air_quality_data(raw: dict) -> dict:
    hourly = raw.get("hourly", {})
    pm2_5 = hourly.get("pm2_5", [None])[-1]
    pm10 = hourly.get("pm10", [None])[-1]
    co = hourly.get("carbon_monoxide", [None])[-1]
    time = hourly.get("time", [None])[-1]
    return {
        "pm2_5": pm2_5,
        "pm2_5_level": get_aqi_level(pm2_5),
        "pm10": pm10,
        "pm10_level": get_aqi_level(pm10),
        "co": co,
        "time": time,
    }

if __name__ == "__main__":
    weather = format_weather_data(get_weather())
    air = format_air_quality_data(get_air_quality())
    print("Weather:", weather)
    print("Air Quality:", air)
