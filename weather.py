import urllib.request, json
from telegram import Update
from telegram.ext import ContextTypes

from APIweatherKey import APIkey
#import requests


async def weather_command(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split()
    city = items[1]
    with urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}&units=metric&lang=ru') as url:
        response = json.loads(url.read().decode())
        main = response['main']
        await update.message.reply_text(f'В городе {city} температура {main["temp"]} °С')