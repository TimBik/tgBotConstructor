import json
from copy import copy

from aiogram import types
from aiogram.types import FSInputFile, CallbackQuery, InlineKeyboardMarkup
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


async def get_builder(message, data):
    builder = InlineKeyboardBuilder()
    buttons = await sync_to_async(message.inline_buttons.all)()
    buttons = await sync_to_async(buttons.order_by)("created")
    print(f"{buttons.__dict__=}")
    buttons_list = await sync_to_async(list)(buttons)

    if message.is_paginate:
        page = data['page']
        if page == -1 or page * 6 >= len(buttons_list):
            raise InvalidPageException()
        end = min(page * 6 + 6, len(buttons_list))

        for i in range(page * 6, end, 2):
            buttons_row = []
            button1: InlineButton = buttons_list[i]
            buttons_row.append(
                types.InlineKeyboardButton(
                    text=await sync_to_async(lambda: button1.text)(),
                    callback_data='{"type":"inline_button", "button_id":"%s", "page":0}' % button1.id
                )
            )
            button2: InlineButton = buttons_list[i + 1] if i + 1 < len(buttons_list) else None
            if button2:
                buttons_row.append(
                    types.InlineKeyboardButton(
                        text=await sync_to_async(lambda: button2.text)(),
                        callback_data='{"type":"inline_button", "button_id":"%s", "page":0}' % button2.id
                    )
                )
            builder.row(*buttons_row)
        buttons_row = []
        data_back = copy(data)
        data_back['page'] = data_back['page'] - 1
        buttons_row.append(
            types.InlineKeyboardButton(
                text="Назад",
                callback_data=json.dumps(data_back)
            )
        )
        data_forward = copy(data)
        data_forward['page'] += 1
        buttons_row.append(
            types.InlineKeyboardButton(
                text="Далее",
                callback_data=json.dumps(data_forward)
            )
        )
        builder.row(*buttons_row)
    else:
        for button in buttons_list:
            button: InlineButton
            builder.row(types.InlineKeyboardButton(
                text=await sync_to_async(lambda: button.text)(),
                callback_data='{"type":"inline_button", "button_id":"%s", "page":0}' % button.id
            ))
    return builder


async def send_inline_message(chat_id, message: InlineMessage, call_back: CallbackQuery, data: dict[str], parse_mode="HTML"):
    try:
        builder = await get_builder(message, data)
    except InvalidPageException:
        await call_back.answer()
        return
    photo = await sync_to_async(lambda: message.image)()
    if photo:
        await bot.send_photo(
            chat_id=chat_id,
            caption=message.text,
            parse_mode=parse_mode,
            reply_markup=builder.as_markup(),
            photo=FSInputFile(f"{photo.name}")
        )
    elif message.update_message:
        await bot.edit_message_text(
            chat_id=call_back.message.chat.id,
            message_id=call_back.message.message_id,
            text=message.text,
            parse_mode=parse_mode,
            reply_markup=builder.as_markup(),
        )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=message.text,
            parse_mode=parse_mode,
            reply_markup=builder.as_markup(),
        )


async def send_message(chat_id, message: Message, call_back: CallbackQuery = None, data=None):
    if isinstance(message, BotMessage):
        await send_bot_message(chat_id, message)
    if isinstance(message, InlineMessage):
        await send_inline_message(chat_id, message, call_back, data)


async def run_events(chat_id, events: list[TgEvent], call_back: CallbackQuery = None, data=None):
    if not events:
        return
    for event in events:
        if not event:
            continue
        message = await sync_to_async(lambda: Message.objects.select_subclasses().get(id=event.message.id))()
        await send_message(chat_id, message, call_back, data)


class DefaultInlineButtonPaginator:
    count = 6


class InvalidPageException(Exception):
    pass
