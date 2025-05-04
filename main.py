from aiogram import Bot, Dispatcher, types

# Directly using the bot token
BOT_TOKEN = "7010529808:AAHUvwwI4-ui3ZmSzu9t0miiSwCrkJUgX5M"  # Replace with your actual token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Hello from Render!")

if __name__ == "__main__":
    dp.run_polling()  # Replace executor with this in aiogram 3.x
