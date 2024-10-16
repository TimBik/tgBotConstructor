from aiogram import types
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, Command
from django.contrib.auth import get_user_model

from tgBot.app import bot
from tgBot.filters.access_rights_filters import AnyUserFilter
from project_settings import ADMINS
from aiogram import types

from tgBot.app import dp


User = get_user_model()


# @dp.message(CommandStart(), AnyUserFilter(), state='*', chat_type=ChatType.PRIVATE)
# async def cmd_start(message: types.Message):
#     user_tg_id = message.from_user.id
#     user = User.objects.get(tg_id=user_tg_id)
#     if user.role != User.Role.ADMIN and user.username in ADMINS:
#         user.role = User.Role.ADMIN
#         user.save(update_fields=['role'])
#     if user.role == User.Role.ADMIN:
#         await bot.send_message(chat_id=user_tg_id, text=f"Приветствую админа {user.username}")
#         await bot.send_message(chat_id=user_tg_id, text=f"я подписал вас на рассылку бота")
#
#     if not (" " in message.text and message.text.split()[1] == "by_qr"):
#         bot.send_message(chat_id=user_tg_id, text="Я отвечаю только тем кто пришел ко мне по QR-коду с колоды")
#         return
#
#     bot.send_message(chat_id=user_tg_id,
#                      text="Приветсвую! Я бот-помощник к вашей колоде) Скоро у меня появится много нового функционала")
#
#

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
