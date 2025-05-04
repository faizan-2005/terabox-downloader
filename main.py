from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

BOT_TOKEN = "7010529808:AAHUvwwI4-ui3ZmSzu9t0miiSwCrkJUgX5M"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Hello from Render!")

if __name__ == "__main__":
    executor.start_polling(dp)
