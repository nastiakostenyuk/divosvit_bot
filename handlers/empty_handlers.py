from bot import dp
from aiogram import types

import parser
from gmail import send_email


@dp.message_handler()
async def send_message(message: types.Message):
    if "повідомлення" in message.text.lower():
        answer = send_email(message.text)
        if answer == 'OK':
            await message.answer('Повідомлення відправлено')
        else:
            await message.answer('Щось пішло не так, спробуй пізніше')
    elif 'товар' in message.text.lower():
        result_parse = parser.search_goods(message.text.lower().replace('товар', ''))
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

    else:
        await message.answer('Ти щось робиш не так, почни з початку!')
