from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

import urllib.request
import json

# Create your views here.

def home(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=b834708621ff9b1359ad8c980f91dfda').read()
            list_of_data = json.loads(source)

            context = {
                "country_code" : str(list_of_data['sys']["country"]),
                "coordinate" : str(list_of_data['coord']["lon"]) +', '+str(list_of_data['coord']["lat"]),
                "temp" : str(list_of_data['main']["temp"]) + ' °C',
                "feels_like" : str(list_of_data['main']["feels_like"]) + ' °C',
                "pressure" : str(list_of_data['main']["pressure"]),
                "humidity" : str(list_of_data['main']["humidity"]),
                "main" : str(list_of_data['weather'][0]["main"]),
                "description" : str(list_of_data['weather'][0]["description"]),
                "icon" : list_of_data['weather'][0]["icon"],
                "city_name" : list_of_data['name'],
            }
            return render(request, 'output.html', context)
    except:
        pass
        
    return render(request, 'home.html',)