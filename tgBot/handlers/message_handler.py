import json

from aiogram import types, F
from aiogram.types import CallbackQuery
from aiogram.utils.callback_answer import CallbackAnswer
from asgiref.sync import sync_to_async

from core.models import InlineButton
from project_settings import MY_TG_ID
from tgBot.app import dp, bot
from tgBot.event_manager import run_events
from tools.logging import get_logging

logger = get_logging(__name__)


@dp.message(F.text)
async def message_handler(msg: types.Message):
    user_id = msg.from_user.id
    await bot.send_message(chat_id=user_id, text="Извините, я вас не понимаю \nПожалуйста воспользуйтесь меню")


@dp.callback_query()
async def message_handler(callback: CallbackQuery):
    try:
        user_id = callback.from_user.id
        print(callback.data)
        data = json.loads(callback.data)
        inline_button_id = data['button_id']
        inline_button = await sync_to_async(
            InlineButton.objects.get
        )(id=inline_button_id)
        await bot.answer_callback_query(callback.id)
        next_event = await sync_to_async(
            lambda: inline_button.next_event
        )()
        await run_events(user_id, [next_event], callback, data)
    except Exception as e:
        if MY_TG_ID:
            await bot.send_message(chat_id=MY_TG_ID, text=e)
        logger.exception(e)