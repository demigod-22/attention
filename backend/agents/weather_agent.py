import requests

# Replace with your API key
WEATHER_API_KEY = "your_openweathermap_api_key"
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, date=None):
    """
    Fetches the current weather for the given city.
    Args:
        city (str): The name of the city.
        date (optional): Currently unused, for potential future expansion.
    Returns:
        dict: Weather details and suggestions.
    """
    try:
        # API request
        response = requests.get(
            WEATHER_API_URL,
            params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
        )
        response.raise_for_status()
        data = response.json()

        # Extract weather information
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        # Create suggestions based on weather
        suggestions = []
        if "rain" in weather:
            suggestions.append("Bring an umbrella as rain is expected.")
        elif "clear" in weather:
            suggestions.append("It's sunny, consider wearing sunscreen.")
        elif "cloud" in weather:
            suggestions.append("It might be cloudy, plan accordingly.")

        if temperature < 10:
            suggestions.append("It's quite cold, bring a jacket.")
        elif temperature > 30:
            suggestions.append("It's hot, stay hydrated and dress lightly.")

        return {
            "city": city,
            "weather": weather,
            "temperature": temperature,
            "feels_like": feels_like,
            "suggestions": suggestions,
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch weather data: {e}"}