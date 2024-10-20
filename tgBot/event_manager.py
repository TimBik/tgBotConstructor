from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async

from core.models import Message, BotMessage, InlineMessage, InlineButton, TgEvent
from tgBot.app import bot


# messages_d = {
#     BotMessage : send_bot_message,
#     InlineMessage: send_inline_message,
# }

async def send_bot_message(chat_id, message: BotMessage):
    await bot.send_message(
        chat_id=chat_id,
        text=message.text,
    )


async def send_inline_message(chat_id, message: InlineMessage):
    builder = InlineKeyboardBuilder()
    buttons = await sync_to_async(message.inline_buttons.all)()
    buttons_list = await sync_to_async(list)(buttons)
    for button in buttons_list:
        button: InlineButton
        builder.row(types.InlineKeyboardButton(
            text=await sync_to_async(lambda: button.text)(),
            callback_data=f"inline_button_{button.id}"
        ))
    await bot.send_message(
        chat_id=chat_id,
        text=await sync_to_async(lambda: message.text)(),
        reply_markup=builder.as_markup()
    )


async def send_message(chat_id, message: Message):
    if isinstance(message, BotMessage):
        await send_bot_message(chat_id, message)
    if isinstance(message, InlineMessage):
        await send_inline_message(chat_id, message)


async def run_events(chat_id, events: list[TgEvent]):
    if not events:
        return
    for event in events:
        message = await sync_to_async(lambda: Message.objects.select_subclasses().get(id=event.message.id))()
        await send_message(chat_id, message)
