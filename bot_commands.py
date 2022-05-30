from telegram import Update
from telegram.ext import ContextTypes
import datetime


async def hi_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'/hi\n/time\n/sum\n/help\n/roshambo')

async def time_command(update: Update, context: ContextTypes):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')