def generate_itinerary(user_preferences):
    city = user_preferences.get("city")
    interests = user_preferences.get("interests", [])
    budget = user_preferences.get("budget", 0)
    # Mock response
    return [
        {"place": "Colosseum", "time": "9:00 AM", "cost": 15, "status": "Open"},
        {"place": "Pantheon", "time": "11:00 AM", "cost": 10, "status": "Open"},
    ]