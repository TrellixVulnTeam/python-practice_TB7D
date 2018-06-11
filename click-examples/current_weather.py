import requests
import click

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

@click.command()
@click.argument('location') 	#Add decorator to main function and give it a name
@click.option('--api-key', '-a', help='your API key for the OpenWeatherMap API',) #Optional arg, with shortcut option
def main(location, api_key): 			#Argument name passed into the wrapped function 
	""" 
	 A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:

    1. London,UK

    2. Canmore

    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
	weather = current_weather(location, api_key)
	print(f"The weather in {location} right now: {weather}.") #string formatting with python 3.6+ 

if __name__ == "__main__":
    main()