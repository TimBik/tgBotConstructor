from aiogram.filters import Command
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model

from core.models import TgEvent, TgEventType, Role
from tgBot.app import bot
from tgBot.event_manager import run_events
from aiogram import types

from tgBot.app import dp

User = get_user_model()


async def get_or_create_user(message: types.Message):
    user, _ = await sync_to_async(User.objects.get_or_create)(
        tg_id=message.from_user.id,
        defaults={
            "tg_id": message.from_user.id,
            "username": message.from_user.username,
            "first_name": message.from_user.first_name ,
            "last_name": message.from_user.last_name if message.from_user.last_name else "",
            "role": Role.AUTHORIZED,
        }
    )
    return user


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    user_tg_id = message.from_user.id
    user = await get_or_create_user(message)
    if user.role == Role.ADMIN:
        await bot.send_message(chat_id=user_tg_id, text=f"Приветствую админа {user.username}")
        return
    if not (" " in message.text and message.text.split()[1] == "by_qr"):
        await bot.send_message(chat_id=user_tg_id, text="Я отвечаю только тем кто пришел ко мне по QR-коду с колоды")
        return

    events = await sync_to_async(TgEvent.objects.filter)(
        type=TgEventType.start_event
    )
    events_list = await sync_to_async(list)(events)
    await run_events(user_tg_id, events_list)
