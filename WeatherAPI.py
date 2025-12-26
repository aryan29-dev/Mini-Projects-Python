import requests

def geocode_city(city: str, country_code: str | None = None):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 10, "language": "en", "format": "json"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    results = data.get("results", [])
    if not results:
        return None
    
    if country_code:
        cc = country_code.strip().upper()
        filtered = [x for x in results if x.get("country_code", "").upper() == cc]
        if filtered:
            results = filtered  # replace results with filtered list

    # If still multiple, prefer higher population if available
    results.sort(key=lambda x: x.get("population", 0), reverse=True)

    top = results[0]
    return {
        "name": top.get("name"),
        "country": top.get("country"),
        "country_code": top.get("country_code"),
        "admin1": top.get("admin1"),   # province/state
        "latitude": top["latitude"],
        "longitude": top["longitude"],
        "timezone": top.get("timezone", "auto"),
    }

def get_forecast(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,windspeed_10m_max,weathercode",
        "timezone": "auto"
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

WEATHER_CODES = {
    0: "Clear",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    61: "Rain",
    71: "Snow",
    80: "Rain showers",
    95: "Thunderstorm",
}

def print_day(daily, i: int):
    date = daily["time"][i]
    tmax = daily["temperature_2m_max"][i]
    tmin = daily["temperature_2m_min"][i]
    wind = daily["windspeed_10m_max"][i]
    code = daily["weathercode"][i]
    desc = WEATHER_CODES.get(code, f"Weather code {code}")

    print(f"{date}:")
    print(f"\tCondition: {desc}")
    print(f"\tHigh: {tmax} °C")
    print(f"\tLow: {tmin} °C")
    print(f"\tWind: {wind} km/h")
    print()

def main():
    city = input("City? ").strip()
    country_code = input("Country Code?").strip().upper()
    if country_code == "":
        country_code = None

    loc = geocode_city(city, country_code)
    if not loc:
        print("Could not find that city.")
        return

    where = f"{loc['name']}"
    if loc.get("admin1"):
        where += f", {loc['admin1']}"
    if loc.get("country"):
        where += f", {loc['country']}"

    print(f"Location found: {where} ({loc['latitude']}, {loc['longitude']})")

    forecast = get_forecast(loc["latitude"], loc["longitude"])
    daily = forecast["daily"]

    print_day(daily, 0)
    print_day(daily, 1)

if __name__ == "__main__":
    main()
