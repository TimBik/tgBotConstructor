from aiogram import types
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from django.contrib.auth import get_user_model

from tgBot.app import dp, bot
from tgBot.filters.access_rights_filters import AnyUserFilter
from tgBot.fsm.admin_user_state import AdminUserState
from tgConstructor.project_settings import ADMINS

User = get_user_model()


@dp.message_handler(CommandStart(), AnyUserFilter(), state='*', chat_type=ChatType.PRIVATE)
async def cmd_start(message: types.Message):
    user_tg_id = message.from_user.id
    user = User.objects.get(tg_id=user_tg_id)
    if user.role != User.Role.ADMIN and user.username in ADMINS:
        user.role = User.Role.ADMIN
        user.save(update_fields=['role'])
    if user.role == User.Role.ADMIN:
        await bot.send_message(chat_id=user_tg_id, text=f"Приветствую админа {user.username}")
        await bot.send_message(chat_id=user_tg_id, text=f"я подписал вас на рассылку бота")
        AdminUserState.start.set()

    if not (" " in message.text and message.text.split()[1] == "by_qr"):
        bot.send_message(chat_id=user_tg_id, text="Я отвечаю только тем кто пришел ко мне по QR-коду с колоды")
        return

    bot.send_message(chat_id=user_tg_id,
                     text="Приветсвую! Я бот-помощник к вашей колоде) Скоро у меня появится много нового функционала")


@bot.message_handler(chat_types=['private'])
def message_handler(msg: types.Message):
    user_id = msg.from_user.id
    bot.send_message(chat_id=user_id, text=msg.text)
