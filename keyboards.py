from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# -----------------------------
# Главное меню
# -----------------------------

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎤 Забронировать")],
        [
            KeyboardButton(text="💰 Цены"),
            KeyboardButton(text="🍽 Меню")
        ],
        [
            KeyboardButton(text="📍 Контакты")
        ]
    ],
    resize_keyboard=True
)

# -----------------------------
# Выбор даты
# -----------------------------

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

# -----------------------------
# Выбор времени
# -----------------------------

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

# -----------------------------
# Кабинки
# -----------------------------

hall_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎤 Мал. кабинка (до 5)")
        ],
        [
            KeyboardButton(text="⭐ Сред. кабинка (до 8)")
        ],
        [
            KeyboardButton(text="👑 Бол. кабинка (до 15)")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

# -----------------------------
# Гости для маленькой кабинки
# -----------------------------

small_guests_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2"),
            KeyboardButton(text="4")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

# -----------------------------
# Гости для средней кабинки
# -----------------------------

medium_guests_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2"),
            KeyboardButton(text="4"),
            KeyboardButton(text="6")
        ],
        [
            KeyboardButton(text="8")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

# -----------------------------
# Гости для большой кабинки
# -----------------------------

large_guests_keyboard = ReplyKeyboardMarkup(
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

# -----------------------------
# Телефон
# -----------------------------

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📱 Отправить номер",
                request_contact=True
            )
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

# -----------------------------
# Подтверждение
# -----------------------------

confirm_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Подтвердить")
        ],
        [
            KeyboardButton(text="❌ Отмена")
        ]
    ],
    resize_keyboard=True
)