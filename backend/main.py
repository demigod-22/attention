from fastapi import FastAPI
from agents.itinerary_agent import generate_itinerary
from agents.optimization_agent import optimize_itinerary
from agents.memory_agent import save_preferences, get_preferences
from agents.weather_agent import get_weather

app = FastAPI()

@app.post("/generate-itinerary/")
async def generate_itinerary_endpoint(user_preferences: dict):
    itinerary = generate_itinerary(user_preferences)
    return {"itinerary": itinerary}

@app.post("/optimize-itinerary/")
async def optimize_itinerary_endpoint(itinerary: dict, constraints: dict):
    optimized_itinerary = optimize_itinerary(itinerary, constraints)
    return {"optimized_itinerary": optimized_itinerary}

@app.post("/save-preferences/")
async def save_preferences_endpoint(user_id: str, preferences: dict):
    save_preferences(user_id, preferences)
    return {"status": "Preferences saved successfully"}

@app.get("/get-weather/")
async def get_weather_endpoint(city: str, date: str):
    weather = get_weather(city, date)
    return {"weather": weather}