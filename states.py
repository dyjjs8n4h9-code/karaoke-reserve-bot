from aiogram.fsm.state import State, StatesGroup


class BookingState(StatesGroup):
    date = State()
    time = State()
    guests = State()
    hall = State()
    phone = State()
    comment = State()