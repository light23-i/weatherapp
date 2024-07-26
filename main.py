import requests

def get_city_coordinates(city, api_key):
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'appid': api_key,
        'limit': 1
    }
    
    response = requests.get(geocoding_url, params=params)
    
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            latitude = location_data[0]['lat']
            longitude = location_data[0]['lon']
            return latitude, longitude
        else:
            print(f"No data found for city: {city}")
            return None, None
    else:
        print(f"Error: Unable to get coordinates for {city}. Status code: {response.status_code}")
        return None, None

def get_weather(lat, lon, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to get weather data. Status code: {response.status_code}")
        return None

def display_weather(city, weather_data):
    if weather_data:
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        weather_desc = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
    else:
        print("No weather data to display.")

# Example usage
api_key = API_KEY
city = "Bareilly"

latitude, longitude = get_city_coordinates(city, api_key)
if latitude and longitude:
    weather_data = get_weather(latitude, longitude, api_key)
    display_weather(city, weather_data)
