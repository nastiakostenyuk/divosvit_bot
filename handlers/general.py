from bot import dp
from aiogram import types


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! щоб побачити мої можливості введіть команду '/about'")


@dp.message_handler(commands=['about'])
async def send_about(message: types.Message):
    await message.reply("Моя задача покращувати рутинні справи! Я можу: \n - робити пошук товару на складах, "
                        "для цього введіть команду '/search_goods' \n "
                        "- надсилати повідомлення керівнику '/send_message'")


@dp.message_handler(commands=['search_goods'])
async def send_goods(message: types.Message):
    await message.answer("Введи потрібний товар, а я пошукаю його на складах\n"
                         "Починай писати товар зі слова: 'Товар'\n"
                         "(Наприклад: Товар: ручка чорна)")


@dp.message_handler(commands=['send_message'])
async def send_message(message: types.Message):
    await message.answer('Введіть повідомлення, які хочете відправити керівнику\n'
                         'Починати повідомлення ОБОВʼЯЗКОВО зі слова: Повідомлення')
