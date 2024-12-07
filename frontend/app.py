import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("One-Day Tour Planning Assistant")

# Collect user preferences
city = st.text_input("Enter the city you want to visit:")
date = st.date_input("Select the date for your trip:")
budget = st.number_input("Enter your budget for the day:", min_value=0)
interests = st.multiselect(
    "Select your interests:", ["Historical Sites", "Food", "Nature", "Shopping"]
)

if st.button("Generate Itinerary"):
    response = requests.post(
        f"{BASE_URL}/generate-itinerary/",
        json={"city": city, "date": str(date), "budget": budget, "interests": interests},
    )
    itinerary = response.json()["itinerary"]
    st.write("Here is your itinerary:")
    for item in itinerary:
        st.write(f"- {item['place']} at {item['time']} (Cost: ${item['cost']})")

# Weather information
if st.button("Check Weather"):
    weather_response = requests.get(f"{BASE_URL}/get-weather/", params={"city": city, "date": str(date)})
    weather = weather_response.json()["weather"]
    st.write("Weather forecast:", weather)