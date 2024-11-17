from aiogram import types
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async

from core.models import Message, BotMessage, InlineMessage, InlineButton, TgEvent
from tgBot.app import bot


# messages_d = {
#     BotMessage : send_bot_message,
#     InlineMessage: send_inline_message,
# }

async def send_bot_message(chat_id, message: BotMessage):
    photo = await sync_to_async(lambda: message.image)()
    file = await sync_to_async(lambda: message.file)()
    if photo:
        await bot.send_photo(
            chat_id=chat_id,
            caption=message.text,
            photo=FSInputFile(f"{photo.name}")
        )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=message.text,
        )
    if file:
        await bot.send_document(
            chat_id=chat_id,
            document=FSInputFile(f"{file.name}")
        )


async def send_inline_message(chat_id, message: InlineMessage, call_back: CallbackQuery):
    builder = InlineKeyboardBuilder()
    buttons = await sync_to_async(message.inline_buttons.all)()
    buttons_list = await sync_to_async(list)(buttons)
    for button in buttons_list:
        button: InlineButton
        builder.row(types.InlineKeyboardButton(
            text=await sync_to_async(lambda: button.text)(),
            callback_data=f"inline_button_{button.id}"
        ))
    photo = await sync_to_async(lambda: message.image)()
    if photo:
        await bot.send_photo(
            chat_id=chat_id,
            caption=message.text,
            reply_markup=builder.as_markup(),
            photo=FSInputFile(f"{photo.name}")
        )
    else:
        if message.update_message:
            await bot.edit_message_text(
                chat_id=call_back.message.chat.id,
                message_id=call_back.message.message_id,
                text=message.text,
            )
            await bot.edit_message_reply_markup(
                chat_id=call_back.message.chat.id,
                message_id=call_back.message.message_id,
                reply_markup=builder.as_markup(),
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=message.text,
                reply_markup=builder.as_markup(),
            )


async def send_message(chat_id, message: Message, call_back: CallbackQuery = None):
    if isinstance(message, BotMessage):
        await send_bot_message(chat_id, message)
    if isinstance(message, InlineMessage):
        await send_inline_message(chat_id, message, call_back)


async def run_events(chat_id, events: list[TgEvent], call_back: CallbackQuery = None):
    if not events:
        return
    for event in events:
        if not event:
            continue
        message = await sync_to_async(lambda: Message.objects.select_subclasses().get(id=event.message.id))()
        await send_message(chat_id, message, call_back)


class DefaultInlineButtonPaginator:
    count = 6

