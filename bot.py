import logging

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
