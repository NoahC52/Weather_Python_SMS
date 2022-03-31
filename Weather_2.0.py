# Imported Modules
import requests
from pyngrok import ngrok
from flask import Flask, request
from signalwire.messaging_response import MessagingResponse
from signalwire.rest import Client as signalwire_client
from dotenv import load_dotenv
import os

load_dotenv()
# For this app you will need a .env with your signalwire credentials, SW phone number, and open-weather API key.
# SIGNALWIRE Specific credentials.
projectID = os.getenv('SIGNALWIRE_PROJECT')
authToken = os.getenv('SIGNALWIRE_TOKEN')
spaceURL = os.getenv('SIGNALWIRE_SPACE')
sw_phone_number = os.getenv('phone_number')

# Global Variables.
# I used the US for this example, but you can put any countries initials here.
country = "us"
api_key = os.getenv('openweather_api')

client = signalwire_client(projectID, authToken, signalwire_space_url=spaceURL)

# Initialize the Flask object
app = Flask(__name__)


# This is the beginning of checking our phone number for any messages.
@app.route("/sms_app", methods=['GET', 'POST'])
def sms_app():
    # Find the body of the incoming message and send out a response based on that string
    body = request.values.get('Body', None)
    url_lat = f"http://api.openweathermap.org/geo/1.0/zip?zip={body},{country}&appid={api_key}"
    response_lat_check = requests.get(url_lat).status_code
    resp = MessagingResponse()
    # Here we begin to check if something went wrong from the initial user response.
    if response_lat_check == 200:
        # With the result being successful, we begin to get the longitude and latitude of the zipcode.
        response = requests.get(url_lat).json()
        lat = response["lat"]
        lon = response["lon"]
        # Printing the response for only us for troubleshooting purposes.
        print(response_lat_check)
        # You can actually convert this into metric units as well! Check open-weathers APIs docs.
        # This is where we actually get the weather data that we use with our longitude and latitude.
        url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat=" \
                      f"{lat}&lon={lon}&appid={api_key}&units=imperial"
        # Here we begin to transfer all our weather data that we want to gather into variables.
        response_weather = requests.get(url_weather).json()
        temp = response_weather["main"]["temp"]
        temp_feel = response_weather["main"]["feels_like"]
        temp = int(temp)
        temp_feel = int(temp_feel)
        name_place = response_weather["name"]
        # With all our data transferred to variables, were finally ready to send it to the end user.
        resp.message("In %s it is currently %d degrees fahrenheit and it feels like %d degrees fahrenheit." % (
            name_place, temp, temp_feel))
        return str(resp)
    else:
        # Since any status code other than 200 means something went wrong, we reply to the user as such.
        resp.message("Sorry, something went wrong. Make sure to enter a US based zipcode!")
        # Printing the response for only us for troubleshooting purposes.
        print(response_lat_check)
        return str(resp)


# These two parts on the very bottom are small code snippets I got from SignalWires troubleshooting docs.
# This opens our port to the internet and allows us to read and send info from the webhook.
def start_ngrok():
    # Set up a tunnel on port 5000 for our Flask object to interact locally
    url = ngrok.connect(5000).public_url
    print(' * Tunnel URL:', url)
    # Now that we have our URL, Use the SignalWire's Update an Incoming Phone Number API
    client.incoming_phone_numbers.list(
        phone_number=sw_phone_number)[0].update(
        sms_url=url + '/sms_app')  # Notice we update the parameter sms_url


if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        start_ngrok()
    app.run(debug=True)
