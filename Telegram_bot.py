
import random
from key import keyboards
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
import asyncio
# import wikipedia
from aiogram.utils.media_group import MediaGroupBuilder
from wikipedia import DisambiguationError
from googletrans import Translator
from Token import TOKEN, API_KEY
import qrcode
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


bot = Bot(token='6430424125:AAEWgGc_2PXtAjMwI28uZp6Rvrzjj773HvQ')
dp = Dispatcher()


@dp.message(CommandStart())
async def message_handler(message: types.Message):
    await message.answer("Barakalla", user_id=2286503)
    await message.answer(f"<b>Assalomu Aleykum</b> men <i>WIKIPEDIA botiman</i> id ,{message.from_user.id}",
                         parse_mode='HTML', reply_markup=keyboards
                         )


user_data = {}
vacancies = {
    'Software Engineer': 'We are looking for a software engineer with 3+ years of experience in Python and JavaScript.',
    'Data Analyst': 'We are looking for a data analyst with experience in SQL and data visualization tools.',
    'Product Manager': 'We are looking for a product manager with experience in agile development methodologies.',
    'UX Designer': 'We are looking for a UX designer with experience in user research and wireframing.',
    'Marketing Manager': 'We are looking for a marketing manager with experience in digital marketing and SEO.',
    'Sales Representative': 'We are looking for a sales representative with experience in B2B sales and CRM software.'
}

invulide_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Vacancies'),
     KeyboardButton(text='My Info', )],
    [KeyboardButton(text='Settings⚙️'),
     KeyboardButton(text='Contact Us')]
], resize_keyboard=True)

vacancies_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
for vacancy in vacancies:
    vacancies_keyboard.keyboard.append([KeyboardButton(text=vacancy)])
vacancies_keyboard.keyboard.append([KeyboardButton(text='Back')])

apply_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
apply_keyboard.keyboard.append([KeyboardButton(text='Yes'), KeyboardButton(text='No')])


@dp.message(Command('start'))
async def command_handler(message: types.Message):
    await message.answer("Welcome to the job bot! Choose an option:", reply_markup=keyboards)
    user_data[message.from_user.id] = {}



@dp.message(F.text == 'Vacancies')
async def vacancies_handler(message: types.Message):
    await message.answer("location hamda nomer yuvoring:", reply_markup=vacancies_keyboard)


@dp.message(F.text.in_(vacancies))
async def vacancy_handler(message: types.Message):
    vacancy = message.text
    description = vacancies[vacancy]
    await message.answer(f"{vacancy}: {description}\n\nWould you like to apply for this position?",
                         reply_markup=apply_keyboard)


@dp.message(F.text.in_(['Yes', 'No']))
async def apple_handler(message: types.Message):
    if message.text == "No":
        user_data[message.from_user.id]['vacancy'] = ""
    await message.answer("Ajoyib Ismingiz nima")


@dp.message(F.text.startswith("+"))
async def phone_handler(message: types.Message):
    if message.text not in user_data[message.from_user.id]:
        user_data[message.from_user.id]['phone'] = message.text
    await message.answer("Raxmat! Sizning kasbingiz nima?")


@dp.message((F.text))
async def name_handler(message: types.Message):
    await message.answer("Raxmat Telefon nomer yuvoring?")

async def main():
    print("Ishlayapti.....")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
