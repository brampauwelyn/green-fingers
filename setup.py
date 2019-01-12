# This script will create a config file
file = open("config.py", "w")
print('GREEN FINGERS')

# Get User Input
country = raw_input("Country from which you want to get the temperature (ISO code) " + "\n" + "-->")
city = raw_input("City to get temperature from" + "\n" + "-->")
unit = raw_input("Unit you want to use to present the temperature " + "\n" + "-->")
weather_api_key = raw_input("You're API Key of openweathermap.org" + "\n" + "-->")
ifttt_key = raw_input("You're API Key of IFTTT" + "\n" + "-->")

# Write settings for IFTTT
file.write("# APIKEY for IFTTT" + "\n")
file.write("IFTTT_KEY = " + "'" + str(ifttt_key) + "'" + "\n")

# Write settings for open weather map API
file.write("# https://openweathermap.org/" + "\n")
file.write("UNIT = " + "'" + str(unit) + "'" + "\n")
file.write("CITY = " + "'" + str(city) + "'" + "\n")
file.write("COUNTRY = " + "'" + str(country) + "'" + "\n")
file.write("WEATHER_API_KEY = " + "'" + str(weather_api_key) + "'" + "\n")
