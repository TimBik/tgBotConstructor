from aiogram import Dispatcher, Bot

from tgConstructor.project_settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()
dp.start_polling(bot)
