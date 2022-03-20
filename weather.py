import json
import tkinter as tk
import requests
import time

from key import API_KEY

def getWeather(canvas):
    city = field.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY
    jsonData = requests.get(api).json()
    condition = jsonData['weather'][0]['main']
    temp = int((jsonData['main']['temp'] - 273.15) * 9/5 + 32)
    minTemp = int((jsonData['main']['temp_min'] - 273.15) * 9/5 + 32)
    maxTemp = int((jsonData['main']['temp_max'] - 273.15) * 9/5 + 32)
    pressure = jsonData['main']['pressure']
    humidity = jsonData['main']['humidity']
    windSpeed = jsonData['wind']['speed']
    windDegree = jsonData['wind']['deg']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(jsonData['sys']['sunrise'] - 14400))
    sunset = time.strftime("%I:%M:%S", time.gmtime(jsonData['sys']['sunset'] - 14400))

    finalInf = condition + "\n" + str(temp) + "° F"
    finalData = "\n" + "Max Temp: " + str(maxTemp) + "° F" + "\n" + "Min Temp: " + str(minTemp) + "° F" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Pressure: " + str(pressure) + " hPa" + "\n" + "Wind Speed: " + str(windSpeed) + " mph " + str(windDegree) + "°" + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = finalInf)
    label2.config(text = finalData)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

field = tk.Entry(canvas, justify= "center", font = t)
field.pack(pady = 20)
field.focus()
field.bind('<Return>', getWeather)


label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()