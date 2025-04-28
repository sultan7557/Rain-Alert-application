import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API credentials from environment
API_URL = "https://api.openweathermap.org/data/2.5/forecast"
weather_api_key = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = f"whatsapp:{os.getenv('TWILIO_FROM_NUMBER')}"
to_number = f"whatsapp:{os.getenv('YOUR_WHATSAPP_NUMBER')}"

# Weather API parameters
params = {
    "lat": float(os.getenv("LATITUDE")),
    "lon": float(os.getenv("LONGITUDE")),
    "appid": weather_api_key,
    "cnt": 4,
}

# Fetch weather data
response = requests.get(API_URL, params=params)
response.raise_for_status()
if response.ok:
    data = response.json()
else:
    print("Request failed:", response.status_code)

# Check weather conditions
will_rain = False
for item in data["list"]:
    weather_id = item["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

# Send message if it will rain
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        body="It's going to rain today. Remember to bring an umbrella!",
        to=to_number
    )
    print("Message sent:", message.sid)
    
    # Check message status
    message_status = client.messages(message.sid).fetch().status
    print(f"Message status: {message_status}")
else:
    print("No rain today.")