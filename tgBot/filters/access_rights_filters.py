from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Filter

from tg_bot.models.User import Role
from tg_bot.services.UserService import user_service


class AnyUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = user_service.create_user_without_phone_by_message_if_doesnt_exist(message)
        return user is not None

class CustomUserFilter(Filter):
    available: Union[Role, list]

    def __init__(self, available: Union[Role, list]):
        self.available = available

    async def check(self, message: types.Message) -> bool:
        user = user_service.create_user_without_phone_by_message_if_doesnt_exist(message)
        if isinstance(self.available, Role):
            return user.role == self.available
        else:
            return user.role in self.available


class NotAnonimUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = user_service.create_user_without_phone_by_message_if_doesnt_exist(message)
        return user is not None and user.role != Role.INCOGNITA
