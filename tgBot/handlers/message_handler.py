from aiogram import types, F

from tgBot.app import dp, bot


@dp.message(F.text)
async def message_handler(msg: types.Message):
    user_id = msg.from_user.id
    # await bot.send_message(chat_id=user_id, text=msg.text)
