from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        """
🌸 سلام خوش اومدی به HFit Coach

من دستیار هوشمند تناسب اندام بانوان هستم.

فعلاً در حال تکمیل هستم و به زودی امکانات زیر فعال میشه:

🥗 برنامه غذایی
🏋️ برنامه تمرینی
🎁 هدیه رایگان
💬 ارتباط با مربی

ممنون که کنار مایی ❤️
"""
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
