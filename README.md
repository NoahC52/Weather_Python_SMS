# Weather_Python_SMS
Text a zip code to the number that you own from SignalWire to begin to receive the weather!
# Hello!
This uses SignalWire and OpenWeather for processing SMS and for gathering the weather! The program scans text from a desired SignalWire number searching for a zip code. It will autoreply either if it doesn't understand or if the API errors out. Once the zip code is received, we run it through OpenWeather's API and get our longitude and latitude. We take the latitude and longitude and run it through another time in the API, this time for the actual weather data. The weather data will be in JSON, so we just use variables to hold the information that we want. We then parse the data in a formatted string and text it back to the user.
# OpenWeather API key & SignalWire
You will need to get your own OpenWeather API key and add it.
https://openweathermap.org/api
This app uses SignalWire For SMS. You will need a account.
https://signalwire.com/
# Other Countries
You can add the initials of other countries as well! Simply go to the "Global Variables" section of code and remove the "US" and put your countries initials!
# User input version
https://github.com/NoahC52/Weather_python_input
