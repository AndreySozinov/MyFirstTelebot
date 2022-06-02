from telegram import Update
from telegram.ext import ContextTypes
from random import randint
from telegram import Update

async def roshambo_command(update: Update, context: ContextTypes):
    await update.message.reply_text("Камень - 0\nНожницы - 1\nБумага-2\n")


async def roshambo_game(update: Update, context: ContextTypes):
    if update.effective_message.text == "0" or update.effective_message.text == "1" or update.effective_message.text == "2":
        list = ['Камень', 'Ножницы', 'Бумага']
        bot_move = randint(0, 2)
        user_move = int(update.effective_message.text)
        if user_move == bot_move: await update.message.reply_text(f"У вас - {list[user_move]}\nУ бота - {list[bot_move]}\nНичья")
        elif (user_move == 0 and bot_move == 1) or (user_move == 1 and bot_move == 2) or (user_move == 2 and bot_move == 0):
            await update.message.reply_text(f"У вас - {list[user_move]}\nУ бота - {list[bot_move]}\nВы победили")
        else: await update.message.reply_text(f"У вас - {list[user_move]}\nУ бота - {list[bot_move]}\nВы проиграли")