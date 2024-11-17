from aiogram import types, F
from aiogram.types import CallbackQuery
from aiogram.utils.callback_answer import CallbackAnswer
from asgiref.sync import sync_to_async

from core.models import InlineButton
from tgBot.app import dp, bot
from tgBot.event_manager import run_events


@dp.message(F.text)
async def message_handler(msg: types.Message):
    user_id = msg.from_user.id
    await bot.send_message(chat_id=user_id, text=msg.text)


@dp.callback_query()
async def message_handler(callback: CallbackQuery):
    user_id = callback.from_user.id
    inline_button_id = callback.data.removeprefix("inline_button_")
    inline_button = await sync_to_async(
        InlineButton.objects.get
    )(id=inline_button_id)
    await bot.answer_callback_query(callback.id)
    next_event = await sync_to_async(
        lambda: inline_button.next_event
    )()
    await run_events(user_id, [next_event], callback)
