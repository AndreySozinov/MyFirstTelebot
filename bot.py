from random import randint
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from bot_commands import *
import TOKEN

async def roshambo_command(update: Update, context: ContextTypes):
    await update.message.reply_text("Камень - 0\nНожницы - 1\nБумага-2\n")


async def roshambo_game(update: Update, context: ContextTypes):
    list = ['Камень', 'Ножницы', 'Бумага']
    bot_move = randint(0, 2)
    user_move = int(update.effective_message.text)
    if user_move == bot_move: await update.message.reply_text(f"У вас - {list[user_move]}\nУ бота - {list[bot_move]}\nНичья")
    elif (user_move == 0 and bot_move == 1) or (user_move == 1 and bot_move == 2) or (user_move == 2 and bot_move == 0):
        await update.message.reply_text(f"У вас - {list[user_move]}\nУ бота - {list[bot_move]}\nВы победили")
    else: await update.message.reply_text(f"У вас - {list[user_move]}\nУ бота - {list[bot_move]}\nВы проиграли")



app = ApplicationBuilder().token(TOKEN.token).build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("roshambo", roshambo_command))
app.add_handler(MessageHandler(filters.TEXT, roshambo_game))


print('server start')
app.run_polling()