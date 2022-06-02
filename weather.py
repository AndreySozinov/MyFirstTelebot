import urllib.request, json
from telegram import Update
from telegram.ext import ContextTypes

from APIweatherKey import APIkey
#import requests


async def weather_command(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split()
    city = items[1]
    print(city)
    with urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}&units=metric&lang=ru') as url:
        response = json.loads(url.read().decode())
        print(response)
        main = response['main']
        print(f'В городе {city}: Температура воздуха {main["temp"]} °С\nОщущается как {main["feels_like"]} °С\nАтмосферное давление {main["pressure"]} hPa\nВлажность {main["humidity"]} %')
        await update.message.reply_text(f'В городе {city}: Температура воздуха {main["temp"]} °С\nОщущается как {main["feels_like"]} °С\nАтмосферное давление {main["pressure"]} hPa\nВлажность {main["humidity"]} %')