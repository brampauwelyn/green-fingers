# This script will create a config file
file = open("config.py", "w")
print('GREEN FINGERS')

# Get User Input
email_address = raw_input("What's your email address to send email notifications" + "\n" + "-->")
password = raw_input("What's your password of your email account" + "\n" + "-->")
from_email = raw_input("The name of the email address which will be used in the email notifications" + "\n" + "-->")
to_email = raw_input("The email adddress to which you want to send the notification" + "\n" + "-->")
country = raw_input("Country from which you want to get the temperature (ISO code) " + "\n" + "-->")
city = raw_input("City to get temperature from" + "\n" + "-->")
unit = raw_input("Unit you want to use to present the temperature " + "\n" + "-->")
weather_api_key = raw_input("You're API Key of openweathermap.org" + "\n" + "-->")

# Write User Input to config.py file
# Write credentials for sending email
file.write("# Credentials for sending email" + "\n")
file.write("USERNAME = " + "'" + str(email_address) + "'" + "\n")
file.write("PASSWORD = " + "'" + str(password) + "'" + "\n")
file.write("FROM_EMAIL = " + "'" + str(from_email) + "'" + "\n")
file.write("TO_EMAIL = " + "'" + str(to_email) + "'" + "\n")
file.write("\n")

# Write settings for open weather map API
file.write("# Credentials for sending email" + "\n")
file.write("# https://openweathermap.org/" + "\n")
file.write("UNIT = " + "'" + str(unit) + "'" + "\n")
file.write("CITY = " + "'" + str(city) + "'" + "\n")
file.write("COUNTRY = " + "'" + str(country) + "'" + "\n")
file.write("WEATHER_API_KEY = " + "'" + str(weather_api_key) + "'" + "\n")
