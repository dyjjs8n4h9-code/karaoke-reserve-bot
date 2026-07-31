from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards import (
    main_keyboard,
    booking_keyboard,
    time_keyboard,
    guests_keyboard,
)
from states import BookingState

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🎤 Добро пожаловать в Karaoke Reserve!\n\n"
        "Выберите действие:",
        reply_markup=main_keyboard
    )


@router.message(F.text == "🎤 Забронировать")
async def booking(message: Message, state: FSMContext):
    await state.set_state(BookingState.date)

    await message.answer(
        "📅 Выберите дату:",
        reply_markup=booking_keyboard
    )


@router.message(
    BookingState.date,
    F.text.in_(["📅 Сегодня", "📅 Завтра", "📆 Послезавтра"])
)
async def choose_date(message: Message, state: FSMContext):

    await state.update_data(date=message.text)

    await state.set_state(BookingState.time)

    await message.answer(
        f"📅 Вы выбрали: {message.text}\n\n"
        "⏰ Теперь выберите время:",
        reply_markup=time_keyboard
    )
    
@router.message(
    BookingState.time,
    F.text.in_(["18:00", "19:00", "20:00", "21:00", "22:00", "23:00"])
)
async def choose_time(message: Message, state: FSMContext):

    await state.update_data(time=message.text)

    await state.set_state(BookingState.guests)

    await message.answer(
        "👥 Сколько будет гостей?",
        reply_markup=guests_keyboard
    )
@router.message(BookingState.guests)
async def choose_guests(message: Message, state: FSMContext):

    await state.update_data(guests=message.text)

    data = await state.get_data()

    await message.answer(
        "✅ Предварительное бронирование\n\n"
        f"📅 {data['date']}\n"
        f"🕒 {data['time']}\n"
        f"👥 {data['guests']}"
    )

    await state.clear()