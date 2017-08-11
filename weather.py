# Function to get weather information from Open Weather Map API
# http://openweathermap.org/api
# Make an account and add your API key in the config.py file (weather_api_key)

def weather():
    import requests
    import json
    # Import your open weather API key from the config file
    from config import UNIT, CITY, COUNTRY, WEATHER_API_KEY
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=%s&APPID=%s" % (CITY, COUNTRY, UNIT, WEATHER_API_KEY)
    print url
    response = requests.get(url)
    content = response.content
    json_data = json.loads(content)
    weather = json_data['main']
    temperature = weather['temp']
    min_temperature = weather['temp_min']
    max_temperature = weather['temp_max']
    print weather
    print temperature
    print min_temperature
