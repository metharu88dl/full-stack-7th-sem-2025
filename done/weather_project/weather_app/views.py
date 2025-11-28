from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def weather_data(request):
    city=request.GET.get('city',"Bengaluru")
    api_key="82e9bee92358da771feb0d350caea1a4"
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(url)
    data=response.json()
    if response.status_code==200 and 'main' in data:
        context={
            'city':city,
            'temperature':data['main']['temp'],
            'description':data['weather'][0]['description'],
            'icon':data['weather'][0]['icon'],
        }
    else:
        context={"error":"City not found"}
    return render(request,'weather_data.html',{"weather":context})
