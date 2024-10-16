from typing import Union

from aiogram import types
from aiogram.filters import Filter
from django.contrib.auth import get_user_model

User = get_user_model()


def create_user_by_message(message: types.Message, role=User.Role.ANONIM):
    try:
        return User.objects.create(
            tg_id=message.from_user.id,
            username=message.from_user.username,
            name=message.from_user.first_name,
            surname=message.from_user.last_name,
            role=role,
        )
    except:
        return None


class AnyUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = create_user_by_message(message)
        return user is not None


class CustomUserFilter(Filter):
    available: Union[User.Role, list]

    def __init__(self, available: Union[User.Role, list]):
        self.available = available

    async def check(self, message: types.Message) -> bool:
        user = create_user_by_message(message)
        if isinstance(self.available, User.Role):
            return user.role == self.available
        else:
            return user.role in self.available


class NotAnonimUserFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        user = create_user_by_message(message)
        return user is not None and user.role != User.Role.ANONIM
