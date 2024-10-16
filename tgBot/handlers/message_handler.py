from aiogram import types

from tgBot.app import dp, bot


@dp.message(chat_types=['private'])
def message_handler(msg: types.Message):
    user_id = msg.from_user.id
    bot.send_message(chat_id=user_id, text=msg.text)
