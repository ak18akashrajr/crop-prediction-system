from predict import predict_we
import geopy
import numpy as np
geolocator = geopy.Nominatim(user_agent="BingBot")
location = "Chennai, Tamil Nadu, India"
geocode = geolocator.geocode(location)
print("Latitude:", geocode.latitude)
print("Longitude:", geocode.longitude)


import requests
lat = 11.0168 # Coimbatore
lon = 76.9558 # Coimbatore

#  API key
api_key = "6a2b15925e074c1f139105aa6f22db53"

#  base URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# complete URL
complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key

#  GET request to the URL
response = requests.get(complete_url)

# Convert the response to JSON format
data = response.json()

# Check the status code of the response
if data["cod"] == 200:
    main = data["main"]
    temp = main["temp"] - 273.15
    feels_like = main["feels_like"] - 273.15
    pressure = main["pressure"]
    humidity = main["humidity"]
    wind = data["wind"]
    wind_speed = wind["speed"]
    visibility = data["visibility"]
    weather = data["weather"]
    description = weather[0]["description"]

    print(predict_we(np.array([temp,feels_like,humidity,wind_speed,visibility,pressure])))
    # Print the results
    print(f"The current temperature at ({lat}, {lon}) is {temp:.2f} °C.")
    print(f"The feels like temperature at ({lat}, {lon}) is {feels_like:.2f} °C.")
    print(f"The current pressure at ({lat}, {lon}) is {pressure} hPa.")
    print(f"The current humidity at ({lat}, {lon}) is {humidity} %.")
    print(f"The current wind speed at ({lat}, {lon}) is {wind_speed} m/s.")
    print(f"The current visibility at ({lat}, {lon}) is {visibility} m.")
    print(f"The current weather at ({lat}, {lon}) is {description}.")
else:
    # Print an error message
    print("Error: Unable to fetch weather data.")




