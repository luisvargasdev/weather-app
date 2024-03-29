import requests

# using API key from OpenWeather website: https://home.openweathermap.org/api_keys
api_key = 'da4d17a34bd3503dbe0c5b1e86910244'

# ask the user for the city to check
user_input = input("Enter city: ")

# from the api it gets the weather data
weather_data =  requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# verify the response from the API is succesfull
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    # to check every variable you can use in a weather application
    # print(weather_data.json())

    # taking some variables to show details to the user
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    # print the results to the user
    print(f"The weather in {user_input} is: {weather}.")
    print(f"The temperature in {user_input} is: {temp}°F.")

