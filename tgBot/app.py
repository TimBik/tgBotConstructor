from aiogram import Dispatcher, Bot
from aiogram.filters import Command

from project_settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
from tgBot.handlers import start_handler


async def start():
    await dp.start_polling(bot)
    dp.message.register(start_handler.cmd_start, Command("start"))
