from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from database.db_session import init_db
from handlers.start import start_command

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.register_message_handler(start_command, commands=['start'])

if __name__ == '__main__':
    init_db()
    executor.start_polling(dp, skip_updates=True)