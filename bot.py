# python3 -m venv .libs
# pip install python-telegram-bot --pre


from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from bot_commands import *
from weather import *
from roshambo import *
import TOKEN


app = ApplicationBuilder().token(TOKEN.token).build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("roshambo", roshambo_command))
app.add_handler(CommandHandler("weather", weather_command))
app.add_handler(MessageHandler(filters.TEXT, roshambo_game))



print('server start')
app.run_polling()