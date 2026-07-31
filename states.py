from aiogram.fsm.state import State, StatesGroup


class BookingState(StatesGroup):
    date = State()
    time = State()
    hall = State()
    guests = State()
    name = State()
    phone = State()
    comment = State()
    confirm = State()
      
