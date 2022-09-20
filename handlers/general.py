import parser
from bot import dp
from aiogram import types
from parser import search_goods



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! щоб побачити мої можливості введіть команду '/about'")


@dp.message_handler(commands=['about'])
async def send_about(message: types.Message):
    await message.reply("Моя задача покращувати рутинні справи! Я можу: \n - робити пошук товару на складах,"
                        "для цього введіть команду '/search_googs' \n - пошук послуги в базі даних '/data_base'")


@dp.message_handler(commands=['search_goods'])
async def send_goods(message: types.Message):
    await message.answer("Введи потрібний товар, а я пошукаю його на складах")


@dp.message_handler()
async def process_start(message: types.Message):
    result_parse = search_goods(message.text)
    if len(result_parse) == 0:
        await message.reply("Нажаль нам нічого не вдалося знайти\n"
                            "Можете перейти на сайт та пошукати товар вручну:\n"
                            "https://akcenter.com.ua/")
    else:
        for model, price, availability, photo, url in result_parse:
            keyboard_1 = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Товар на сайті", url=url)
            keyboard_1.add(url_button)
            await message.answer(f"{model}\n{price}\n{availability}\n{photo}", reply_markup=keyboard_1)

        keyboard_2 = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт", url=parser.url)
        keyboard_2.add(url_button)
        await message.answer("Більше товару на сайті", reply_markup=keyboard_2)
