# Rain Alert Application

A Python application that checks the weather forecast and sends a WhatsApp message if rain is expected.

## Features

- Fetches weather forecast from OpenWeatherMap API
- Checks if rain is predicted in the next few hours
- Sends automated WhatsApp alerts via Twilio

## Setup

1. Clone this repository
2. Install requirements:

pip install -r requirements.txt

3. Create a `.env` file based on `.env.example` with your actual API keys
4. Run the script:

python main.py


## Environment Variables

Copy `.env.example` to `.env` and fill in your details:

- `WEATHER_API_KEY`: Your OpenWeatherMap API key
- `LATITUDE` and `LONGITUDE`: Your location coordinates
- `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`: Your Twilio credentials
- `TWILIO_FROM_NUMBER`: Twilio's WhatsApp number
- `YOUR_WHATSAPP_NUMBER`: Your WhatsApp number

## Usage

Set up as a scheduled task or cron job to run daily before you leave home.
