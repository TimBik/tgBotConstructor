from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminUserState(StatesGroup):
    start = State()
    # get_all_application = State()