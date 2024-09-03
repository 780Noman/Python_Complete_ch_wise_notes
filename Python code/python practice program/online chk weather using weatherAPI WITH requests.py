#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     11/07/2023
# Copyright:   (c) DELL 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def main():
##    pass
##
##if __name__ == '__main__':
##    main()
import requests

def get_weather(city):
    api_key = "bcd587ce2a154076b1765001231107&q=Rawalpindi"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 404:
        return "City not found"

    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    return f"Weather in {city}: {weather_description}\nTemperature: {temperature}°F\nHumidity: {humidity}%"

def main():
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    print(weather_info)

if __name__ == "__main__":
      main()
