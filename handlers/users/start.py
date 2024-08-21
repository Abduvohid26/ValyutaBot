from http.client import responses

from aiogram.filters import CommandStart
from loader import dp, db, bot
from aiogram import types, F
from keyboards.default.buttons import type_buttons
import requests


url = 'http://nbu.uz/uz/exchange-rates/json/'
proxies = {
    'http': None,
    'https': None,
}
response = requests.get(url=url, proxies=proxies)
datas = response.json()


@dp.message(CommandStart())
async def start_bot(message:types.Message):
    if db.select_user(id=message.from_user.id):
        pass
    else:
        db.add_user(id=message.from_user.id, fullname=message.from_user.full_name, telegram_id=message.from_user.id,
                    language=message.from_user.language_code)
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!", reply_markup=type_buttons())



@dp.message(F.text)
async def check_and_get(message: types.Message):
    course = message.text.split(',')[-1].strip()
    title = message.text
    for data in datas:
        if  data['code'] == course:
            await message.answer(f'{title}\n'
                                 f'💸 Sotib olish: {data["nbu_buy_price"]}\n'
                                 f'💰 Sotish: {data["nbu_cell_price"]}\n'
                                 f'📆 Sana: {data["date"]}')
        else:
            pass
    await message.answer('🤖 Botdan foydalanganingiz uchun rahmat.')

