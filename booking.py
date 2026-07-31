from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards import (
    main_keyboard,
    booking_keyboard,
    time_keyboard,
    hall_keyboard,
    small_guests_keyboard,
    medium_guests_keyboard,
    large_guests_keyboard,
    phone_keyboard,
    confirm_keyboard,
)

from states import BookingState

from database import (
    add_booking,
    get_bookings,
)

router = Router()


# ==========================
# START
# ==========================

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):

    await state.clear()

    await message.answer(
        "🎤 <b>Karaoke Reserve</b>\n\n"
        "Добро пожаловать!\n\n"
        "Выберите действие:",
        reply_markup=main_keyboard
    )


# ==========================
# НАЧАТЬ БРОНЬ
# ==========================

@router.message(F.text == "🎤 Забронировать")
async def booking(message: Message, state: FSMContext):

    await state.clear()

    await state.set_state(BookingState.date)

    await message.answer(
        "──────────────\n"
        "📅 <b>Выберите дату</b>",
        reply_markup=booking_keyboard
    )


# ==========================
# ДАТА
# ==========================

@router.message(
    BookingState.date,
    F.text.in_([
        "📅 Сегодня",
        "📅 Завтра",
        "📆 Послезавтра"
    ])
)
async def choose_date(message: Message, state: FSMContext):

    await state.update_data(
        date=message.text
    )

    await state.set_state(
        BookingState.time
    )

    await message.answer(
        "──────────────\n"
        "🕒 <b>Выберите время</b>",
        reply_markup=time_keyboard
    )


# ==========================
# ВРЕМЯ
# ==========================

@router.message(
    BookingState.time,
    F.text.in_([
        "18:00",
        "19:00",
        "20:00",
        "21:00",
        "22:00",
        "23:00",
    ])
)
async def choose_time(message: Message, state: FSMContext):

    await state.update_data(
        time=message.text
    )

    await state.set_state(
        BookingState.hall
    )

    await message.answer(
        "──────────────\n"
        "🏠 <b>Выберите кабинку</b>",
        reply_markup=hall_keyboard
    )


# ==========================
# КАБИНКА
# ==========================

@router.message(
    BookingState.hall,
    F.text.in_([
        "🎤 Мал. кабинка (до 5)",
        "⭐ Сред. кабинка (до 8)",
        "👑 Бол. кабинка (до 15)",
    ])
)
async def choose_hall(message: Message, state: FSMContext):

    hall = message.text

    await state.update_data(
        hall=hall
    )

    await state.set_state(
        BookingState.guests
    )

    if hall == "🎤 Мал. кабинка (до 5)":

        keyboard = small_guests_keyboard

    elif hall == "⭐ Сред. кабинка (до 8)":

        keyboard = medium_guests_keyboard

    else:

        keyboard = large_guests_keyboard

    await message.answer(
        "──────────────\n"
        "👥 <b>Количество гостей</b>",
        reply_markup=keyboard
    )


# ==========================
# ГОСТИ
# ==========================

@router.message(
    BookingState.guests,
    F.text.in_(["2", "4", "6", "8", "10", "12+"])
)
async def choose_guests(message: Message, state: FSMContext):

    await state.update_data(
        guests=message.text
    )

    await state.set_state(
        BookingState.name
    )

    await message.answer(
        "──────────────\n"
        "👤 <b>Введите Ваше имя</b>"
    )


# ==========================
# ИМЯ
# ==========================

@router.message(BookingState.name)
async def choose_name(message: Message, state: FSMContext):

    await state.update_data(
        name=message.text
    )

    await state.set_state(
        BookingState.phone
    )

    await message.answer(
        "──────────────\n"
        "📱 <b>Отправьте номер телефона</b>",
        reply_markup=phone_keyboard
    )


# ==========================
# ТЕЛЕФОН
# ==========================

@router.message(
    BookingState.phone,
    F.contact
)
async def choose_phone(message: Message, state: FSMContext):

    await state.update_data(
        phone=message.contact.phone_number
    )

    await state.set_state(
        BookingState.comment
    )

    await message.answer(
        "──────────────\n"
        "📝 <b>Комментарий к бронированию</b>\n\n"
        "Если комментария нет — напишите <b>Нет</b>."
    )


# ==========================
# КОММЕНТАРИЙ
# ==========================

@router.message(BookingState.comment)
async def choose_comment(message: Message, state: FSMContext):

    await state.update_data(
        comment=message.text
    )

    await state.set_state(
        BookingState.confirm
    )

    data = await state.get_data()

    await message.answer(
        "──────────────\n"
        "📋 <b>Проверьте бронирование</b>\n\n"
        f"📅 {data['date']}\n"
        f"🕒 {data['time']}\n"
        f"🏠 {data['hall']}\n"
        f"👥 {data['guests']}\n"
        f"👤 {data['name']}\n"
        f"📱 {data['phone']}\n"
        f"📝 {data['comment']}",
        reply_markup=confirm_keyboard
    )

# ==========================
# ПОДТВЕРЖДЕНИЕ
# ==========================

@router.message(
    BookingState.confirm,
    F.text == "✅ Подтвердить"
)
async def confirm_booking(message: Message, state: FSMContext):

    data = await state.get_data()

    await add_booking(
        data["date"],
        data["time"],
        data["hall"],
        data["guests"],
        data["name"],
        data["phone"],
        data["comment"]
    )

    await message.answer(
        "✅ <b>Бронирование успешно создано!</b>\n\n"
        "Спасибо за бронирование!\n"
        "Мы свяжемся с Вами для подтверждения.",
        reply_markup=main_keyboard
    )

    await state.clear()


# ==========================
# ОТМЕНА
# ==========================

@router.message(
    BookingState.confirm,
    F.text == "❌ Отмена"
)
async def cancel_booking(message: Message, state: FSMContext):

    await state.clear()

    await message.answer(
        "❌ Бронирование отменено.",
        reply_markup=main_keyboard
    )


# ==========================
# АДМИН
# ==========================

@router.message(Command("admin"))
async def admin_panel(message: Message):

    bookings = await get_bookings()

    if not bookings:
        await message.answer("Бронирований пока нет.")
        return

    text = "<b>📋 Все бронирования</b>\n\n"

    for booking in bookings:

        (
            booking_id,
            date,
            time,
            hall,
            guests,
            name,
            phone,
            comment,
            status
        ) = booking

        text += (
            f"🆔 #{booking_id}\n"
            f"📅 {date}\n"
            f"🕒 {time}\n"
            f"🏠 {hall}\n"
            f"👥 {guests}\n"
            f"👤 {name}\n"
            f"📱 {phone}\n"
            f"📝 {comment}\n"
            f"📌 {status}\n\n"
        )

    await message.answer(text)