import requests

city = input("Enter your city name: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

try:
    geo_response = requests.get(geo_url)

    if geo_response.status_code != 200:
        print("Error fetching location data")
        exit()

    geo_data = geo_response.json()

    if "results" not in geo_data:
        print("City not found")
        exit()

    result = geo_data["results"][0]

    latitude = result["latitude"]
    longitude = result["longitude"]
    city_name = result["name"]

except requests.exceptions.RequestException:
    print("Network error (location)")
    exit()

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

try:
    weather_Response = requests.get(weather_url)

    if weather_Response.status_code != 200:
        print("Error fetching weather data")
        exit()

    weather_data = weather_Response.json()

    weather = weather_data["current_weather"]

    temp_c = weather["temperature"]
    wind_speed = weather["windspeed"]
    weather_code = weather["weathercode"]

    temp_f = (temp_c * 9/5) + 32

    print("\n==== weather ===")
    print("City:", city_name)
    print("Temperature:", temp_c, "°C /", round(temp_f, 2), "°F")
    print("Wind Speed:", wind_speed, "km/h")
    print("weather code:", weather_code)

except requests.exceptions.RequestException:
    print("Network error Weather")


