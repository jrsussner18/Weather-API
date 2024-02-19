# Jake Sussner
# Weather API
# 02 - 18 - 24

# import libraries
import datetime as dt
import requests
import key


# function to convert kelvin to fahrenheit
def k_to_f(kelvin):
    fahrenheit = (kelvin - 273.15) * (9 / 5) + 32
    return fahrenheit


# function to return wind speed and direction
def wind_velocity(wind_speed_ms, direction_deg):
    # Convert wind speed from m/s to mph
    wind_speed_mph = wind_speed_ms * 2.23694

    # Define wind direction based on degree range
    if 348.75 <= direction_deg < 11.25:
        wind_direction = "N"
    elif 11.25 <= direction_deg < 33.75:
        wind_direction = "NNE"
    elif 33.75 <= direction_deg < 56.25:
        wind_direction = "NE"
    elif 56.25 <= direction_deg < 78.75:
        wind_direction = "ENE"
    elif 78.75 <= direction_deg < 101.25:
        wind_direction = "E"
    elif 101.25 <= direction_deg < 123.75:
        wind_direction = "ESE"
    elif 123.75 <= direction_deg < 146.25:
        wind_direction = "SE"
    elif 146.25 <= direction_deg < 168.75:
        wind_direction = "SSE"
    elif 168.75 <= direction_deg < 191.25:
        wind_direction = "S"
    elif 191.25 <= direction_deg < 213.75:
        wind_direction = "SSW"
    elif 213.75 <= direction_deg < 236.25:
        wind_direction = "SW"
    elif 236.25 <= direction_deg < 258.75:
        wind_direction = "WSW"
    elif 258.75 <= direction_deg < 281.25:
        wind_direction = "W"
    elif 281.25 <= direction_deg < 303.75:
        wind_direction = "WNW"
    elif 303.75 <= direction_deg < 326.25:
        wind_direction = "NW"
    else:
        wind_direction = "NNW"

    return wind_speed_mph, wind_direction


# getting city and state or country from user
city = input("What city are you finding the weather for? (ie. New York)")
location = input("What state or country is this city in?")
url = url = (
    f"http://api.openweathermap.org/data/2.5/weather?q={city},{location}&appid={key.API_KEY}"
)

# get data from openweathermap
response = requests.get(url)

# validate city and state or country
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
    print(data)
else:
    raise ValueError("Failed to fetch data from OpenWeatherMap API")


# get the weather data
temp_fahrenheit = k_to_f(data["main"]["temp"])
temp_high = k_to_f(data["main"]["temp_max"])
temp_low = k_to_f(data["main"]["temp_min"])
sunrise_time = dt.datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"])
sunset_time = dt.datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"])
humidity = data["main"]["humidity"]
wind, direction = wind_velocity(data["wind"]["speed"], data["wind"]["deg"])

# output the data
print(f"The current temperature is {temp_fahrenheit:.2f}°F")
print(f"Today's high is {temp_high:.2f}°F")
print(f"Today's low is {temp_low:.2f}°F")
print(f"The humidity is {humidity}%")
print(f"The wind is traveling {direction} at {wind:.2f} mph")
print(f"Today's sunrise: {sunrise_time} a.m.")
print(f"Today's sunset: {sunset_time} p.m.")
