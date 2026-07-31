from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎤 Забронировать")],
        [KeyboardButton(text="💰 Цены"), KeyboardButton(text="🍽 Меню")],
        [KeyboardButton(text="📍 Контакты")]
    ],
    resize_keyboard=True
)
booking_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Сегодня"),
            KeyboardButton(text="📅 Завтра")
        ],
        [
            KeyboardButton(text="📆 Послезавтра")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)
time_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="18:00"),
            KeyboardButton(text="19:00")
        ],
        [
            KeyboardButton(text="20:00"),
            KeyboardButton(text="21:00")
        ],
        [
            KeyboardButton(text="22:00"),
            KeyboardButton(text="23:00")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)
guests_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2"),
            KeyboardButton(text="4"),
            KeyboardButton(text="6")
        ],
        [
            KeyboardButton(text="8"),
            KeyboardButton(text="10"),
            KeyboardButton(text="12+")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)