from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime
import random
import ai_code_1


TOKEN = "8124674739:AAEeF30hUe4Spq7jvTbOp4y1PMakyDscncQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Что я умею:\n"
        "/start - запуск бота\n"
        "/help - список команд\n"
        "/time  - текущее время\n"
        "/joke - случайная шутка\n"
    )
    await update.message.reply_text(text)
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime('%H:%M:%S')
    await update.message.reply_text(f"Сейчас {now}")

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Почему программисты путают Хеллоуин и Рождество? Потому что Oct 31 == Dec 25.",
        "На 99% готово - это когда осталось только переписать.",
        "Программисты не тонут. Они просто идут в отладку."
    ]
    await update.message.reply_text(random.choice(jokes))



    
if __name__ == '__main__': #запуск бота
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("startai", ai_code_1.startai))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("joke", joke_command))
    app.add_handler(CommandHandler("ask", ai_code_1.ask_command))
    #app.add_handler(MessageHandler(" ", ai_code_1.ask_command))
    
    
    print("Бот запущен..")
    app.run_polling()
    