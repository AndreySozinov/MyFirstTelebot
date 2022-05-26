from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def logging(update: Update, context: ContextTypes.context):
    file = open('logs.csv', 'a')
    file.write(f'{update.effective_user.id},{update.effective_user.first_name},{update.message.text}\n')
    file.close()