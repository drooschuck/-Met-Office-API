from django.shortcuts import render
from django.http import JsonResponse
from .models import whole_city
import json
import requests


def convert_temperature(temp, unit):
    if unit == 'F':
        return (temp - 32) * 5.0 / 9.0  # Convert Fahrenheit to Celsius
    elif unit == 'K':
        return temp - 273.15  # Convert Kelvin to Celsius
    else:
        return temp  # Assume it's already in Celsius

def weather(request):
    if 'location' in request.GET:
        city = request.GET.get('location')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4c2d63a9ff3a8181c364c2ee103f4559"  # Replace YOUR_API_KEY with your actual API key
        x = requests.get(url)
        
        # Converts response object to dictionary
        y = x.json()
        
        # Convert temperature from Kelvin to Celsius
        temp_celsius = convert_temperature(y['main']['temp'], 'K')

        context = {
            'city_name': f"City name: {y['name']}",
            'Temp': f"Temperature: {temp_celsius:.2f} °C",  # Display in Celsius
            'Pressure': f"Pressure: {y['main']['pressure']} hPa",
            'Humidity': f"Humidity: {y['main']['humidity']} %",
            'Weather_condition': f"Weather Condition: {y['weather'][0]['description'].upper()}"
        }

        return render(request, 'home.html', context)
    
    return render(request, 'home.html')

#def weather(request):
 #   if 'location' in request.GET:
  #      city = request.GET.get('location')
   #     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4c2d63a9ff3a8181c364c2ee103f4559"
        # demonstrate how to use the 'params' parameter:
    #    x = requests.get(url)
        #Converts response object to dictionary
     #   y = x.json()
      #  context = {
       #     'city_name' : f"City name: {y['name']}",
        #    'Temp': f"Temperature: {y['main']['temp']} F",
         #   'Pressure': f"Pressure: {y['main']['pressure']}",
          #  'Humidity': f"Humidity: {y['main']['humidity']}",
           # 'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
       # }

        # return render(request, 'home.html', context)
    # return render(request, 'home.html')


#datahub api - regiter and test api 
"""
from django.shortcuts import render
from django.http import JsonResponse
import requests

def convert_temperature(temp, unit):
    if unit == 'F':
        return (temp - 32) * 5.0 / 9.0  # Convert Fahrenheit to Celsius
    elif unit == 'K':
        return temp - 273.15  # Convert Kelvin to Celsius
    else:
        return temp  # Assume it's already in Celsius

def weather(request):
    if 'location' in request.GET:
        city = request.GET.get('location')
        
        # Replace the following URL with the actual DataHub API endpoint for weather
        url = f"https://api.datahub.io/weather/site-specific?location={city}"  # Example URL
        
        # Perform the API request
        response = requests.get(url)
        
        if response.status_code == 200:
            # Converts response object to dictionary
            weather_data = response.json()
            
            # Assuming the DataHub API returns temperature in Kelvin
            temp_celsius = convert_temperature(weather_data['temperature'], 'K')

            context = {
                'city_name': f"City name: {weather_data['city']}",
                'Temp': f"Temperature: {temp_celsius:.2f} °C",  # Display in Celsius
                'Pressure': f"Pressure: {weather_data['pressure']} hPa",
                'Humidity': f"Humidity: {weather_data['humidity']} %",
                'Weather_condition': f"Weather Condition: {weather_data['condition'].upper()}"
            }
        else:
            context = {
                'error': f"Could not retrieve weather data for {city}. Please try again."
            }

        return render(request, 'home.html', context)
    
    return render(request, 'home.html')
"""