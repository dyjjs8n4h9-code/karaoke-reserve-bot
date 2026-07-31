import aiosqlite

DB_NAME = "karaoke.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                hall TEXT NOT NULL,
                guests TEXT NOT NULL,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                comment TEXT,
                status TEXT DEFAULT 'Новая'
            )
        """)

        await db.commit()


async def add_booking(
    date,
    time,
    hall,
    guests,
    name,
    phone,
    comment
):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT INTO bookings
            (
                date,
                time,
                hall,
                guests,
                name,
                phone,
                comment
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                date,
                time,
                hall,
                guests,
                name,
                phone,
                comment
            )
        )

        await db.commit()


async def get_bookings():
    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute("""
            SELECT
                id,
                date,
                time,
                hall,
                guests,
                name,
                phone,
                comment,
                status
            FROM bookings
            ORDER BY id DESC
        """)

        rows = await cursor.fetchall()

        return rows


async def delete_booking(booking_id):
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            "DELETE FROM bookings WHERE id = ?",
            (booking_id,)
        )

        await db.commit()


async def update_status(booking_id, status):
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            UPDATE bookings
            SET status = ?
            WHERE id = ?
            """,
            (
                status,
                booking_id
            )
        )

        await db.commit()