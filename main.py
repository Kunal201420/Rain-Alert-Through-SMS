import requests
import os

from twilio.rest import Client

weather_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")


parameters = {
    "key" : weather_key,
    "q" : "chinchwad",
    "days" : 1,
    "aqi" : "no",
    "alerts" : "no"
}


response = requests.get("https://api.weatherapi.com/v1/forecast.json" , params=parameters)
response.raise_for_status()
data = response.json()
will_it_rain = data["forecast"]["forecastday"][0]["hour"][0]["will_it_rain"]



if will_it_rain == 1:
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+918624807815",
        from_="+16073884532",
        body="It will Rain today! Please bring an Umbrella!☔")


else:
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+918624807815",
        from_="+16073884532",
        body="It's a Sunny day!🌞")



