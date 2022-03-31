# Weather_Python_SMS
Text a zip code to the number that you own from SignalWire to begin to receive the weather!
# Hello!
This weather app I built uses OpenWeather's API for delivering weather based on zip code!
This version is much simpler than the SMS based one, all it uses is one input from the user asking them for the zip code. We take the zip code and transfer it to the API to convert the zip code into longitude and latitude. We then take the longitude and latitude and use the API once more to get the weather data, the data will be in JSON, so we will just setup variables to hold parsed data for us. After all said is done we format it and print it out to the user.
# OpenWeather API key
You will need to get your own API key and add it. 
https://openweathermap.org/api
# Other Countries
You can add the initials of other countries as well! Simply go to the "Global Variables" section of code and remove the "US" and put your countries initials!
# SMS Version
