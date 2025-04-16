# import nest_asyncio
# nest_asyncio.apply()

# import asyncio
# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from apscheduler.schedulers.asyncio import AsyncIOScheduler

# # Налаштування логування
# logging.basicConfig(level=logging.INFO)

# # Токен бота (замініть на свій)
# BOT_TOKEN = "7914517419:AAHMV6VpW6u6oAGcSy9i0cRM1Dro8_WDmdk"

# # Множина для зберігання chat_id користувачів, які викликали команду /start
# chat_ids = set()

# # Обробник команди /start: зберігаємо chat_id та надсилаємо відповідь
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat_id = update.effective_chat.id
#     chat_ids.add(chat_id)
#     await update.message.reply_text(f"Бот працює. Ваш chat_id: {chat_id}")

# # Функція для надсилання щоденного повідомлення всім збереженим chat_id
# async def send_daily_message(application):
#     print("⏰ Виконано задачу: надсилання повідомлення")
#     for chat_id in chat_ids:
#         try:
#             await application.bot.send_message(
#                 chat_id=chat_id, text="Це щоденне повідомлення! 🌞"
#             )
#         except Exception as e:
#             logging.error(f"Помилка при надсиланні повідомлення користувачу {chat_id}: {e}")

# # Основна асинхронна функція, що налаштовує бота і планувальник
# async def main():
#     # Створення додатку бота
#     application = ApplicationBuilder().token(BOT_TOKEN).build()

#     # Додавання обробника команди /start
#     application.add_handler(CommandHandler("start", start))

#     # Налаштування асинхронного планувальника (APScheduler) з таймзоною "Europe/Kyiv"
#     scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")
#     # Додавання завдання: щодня о 10:00 надсилати повідомлення (функція send_daily_message)
#     scheduler.add_job(send_daily_message, trigger="cron", hour=23, minute=56, args=[application])
#     scheduler.start()

#     print("🚀 Бот запущено. Слухаємо команди та очікуємо щоденне надсилання...")

#     # Запуск бота: параметр close_loop=False запобігає спробі закрити запущений event loop
#     await application.run_polling(close_loop=False)

# if __name__ == "__main__":
#     # Використання asyncio.run для запуску основної функції в асинхронному середовищі
#     asyncio.run(main())


from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Update
from telegram.ext import Application, ContextTypes
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Твій chat_id (заміни на свій)
CHAT_ID = '-4040228119'

# Функція для надсилання повідомлення
async def send_daily_message(application: Application):
    # Відправка повідомлення на вказаний chat_id
    await application.bot.send_message(chat_id=CHAT_ID, text="Привіт,йопта")

# Основна функція для запуску бота
async def main():
    # Створення додатку бота
    application = Application.builder().token("7914517419:AAHMV6VpW6u6oAGcSy9i0cRM1Dro8_WDmdk").build()

    # Налаштування асинхронного планувальника (APScheduler) з таймзоною "Europe/Kyiv"
    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")
    # Додавання завдання: щодня о 23:46 надсилати повідомлення (функція send_daily_message)
    scheduler.add_job(send_daily_message, trigger="cron", hour=00, minute=11, args=[application])
    
    # Запуск планувальника
    scheduler.start()

    # Запуск бота на прослуховування команд
    await application.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()  # Додатково для запуску асинхронних задач в Jupyter чи середовищах з активними циклічними подіями
    import asyncio
    asyncio.run(main())  # Запуск основної функції
