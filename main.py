

from keep_alive import keep_alive
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Update
from telegram.ext import Application, ContextTypes
import logging
from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# async def get_custom_emoji_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if update.message and update.message.entities:
#         for entity in update.message.entities:
#             if entity.type == "custom_emoji":
#                 await update.message.reply_text(
#                     f"🆔 Emoji ID: `{entity.custom_emoji_id}`",
#                     parse_mode="Markdown"
#                 )     


# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Твій chat_id (заміни на свій)
CHAT_ID = '-1001964846494'
TEXT_1 = """ 
🔥  Леді та Джентльмени! 🔥
💎 Касир Поліна на зв'язку! 💎
⚡ Реквізити тут — @KaSSa_4444! ⚡
 """

TEXT_2 = """ 
🎁 ЩОДЕННИЙ БОНУС! 🎲

Поповнив рахунок? Лови шанс на приємний сюрприз!

Одразу після депозиту — переходь у чат із касиром та кидай кубик удачі!

🔹 1–3 — ех, спроба була невдалою 😢

🔹 4–6 — ВІТАЄМО! 🎉 Твій бонус — 50 грн до депозиту ! 💸

❗️ Бонусні гроші віднімаються при виводі.
 """

TEXT_3 = """ 
🔐 СЕЙФ — Грошовий квест починається! 💥
 
⚡️ У нас є віртуальний сейф, у якому захований грошовий приз:

 👻 2️⃣0️⃣0️⃣0️⃣ грн 

🔸Грай на наших слотах та впіймай бонус 2️⃣0️⃣0️⃣ грн.

🔸Скинь скрін виграшу в групу та обери свій щасливий номер.
 """

TEXT_4 = """ 
🔁 ОТРИМАЙ ВІДКАТ 10% 💵


🎯 Граєш на великі ставки? Ми дбаємо про твою удачу!

💰 Отримай 10% кешбек, якщо зробив депозит від 1️⃣0️⃣0️⃣0️⃣ грн

 📆 Рахується щодня — шанс повернути частину й спробувати ще раз!
 """

TEXT_5 = """ 
🎰 БОНУС НА SUPEROMATIC! 💸


🔥 Бонус додається на кожен депозит від 300 грн

📅 Пн – Чт — отримуй +10% до депозиту

📅 Пт – Нд — вже +20% на рахунок!

💥 Лови виграш, поки гаряче — Superomatic заряджений на фортуну! 🍀

💳 Бонус нараховується одразу після поповнення рахунку❗️ При виводі бонуси віднімаються❗️
"""

TEXT_6 = """ 

 """

TEXT_7 = """ 

 """




# @application.message()
async def get_custom_emoji_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.entities:
        for entity in update.message.entities:
            if entity.type == "custom_emoji":
                await update.message.reply_text(f"🆔 Emoji ID: `{entity.custom_emoji_id}`")

# Функція для надсилання повідомлення
async def send_daily_message(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_1 )

async def send_daily_message2(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_2 )

async def send_daily_message3(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_3 )    

async def send_daily_message4(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_4 )

async def send_daily_message5(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_5 )

async def send_daily_message6(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_3 )

async def send_daily_message7(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_2 )

async def send_daily_message8(application: Application):
   
    await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_4 )

# async def send_daily_message9(application: Application):
   
#     await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_2 )

# async def send_daily_message10(application: Application):
   
#     await application.bot.send_message(chat_id=CHAT_ID, text=TEXT_2 )


# Основна функція для запуску бота
async def main():
    # Створення додатку бота
    keep_alive()
    application = Application.builder().token("7688368621:AAFoSxcstDmbp9hhuxbDk2bvkS01KXrsz2U").build()

    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")
 
    scheduler.add_job(send_daily_message, trigger="cron", hour=10, minute=00, args=[application])
    scheduler.add_job(send_daily_message2, trigger="cron", hour=11, minute=00, args=[application])
    scheduler.add_job(send_daily_message3, trigger="cron", hour=12, minute=00, args=[application])
    scheduler.add_job(send_daily_message4, trigger="cron", hour=15, minute=00, args=[application])
    scheduler.add_job(send_daily_message5, trigger="cron", hour=18, minute=00, args=[application])
    scheduler.add_job(send_daily_message6, trigger="cron", hour=19, minute=00, args=[application])
    scheduler.add_job(send_daily_message7, trigger="cron", hour=20, minute=00, args=[application])
    scheduler.add_job(send_daily_message8, trigger="cron", hour=21, minute=00, args=[application])
    # scheduler.add_job(send_daily_message9, trigger="cron", hour=21, minute=00, args=[application])
    # scheduler.add_job(send_daily_message10, trigger="cron", hour=21, minute=00, args=[application])

    # Запуск планувальника
    scheduler.start()

    # Запуск бота на прослуховування команд
    await application.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()  # Додатково для запуску асинхронних задач в Jupyter чи середовищах з активними циклічними подіями
    import asyncio
    asyncio.run(main())  # Запуск основної функції
