
import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from Token import TOKEN
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

from key import main_keyboard, vacancies_keyboard, vacancies, apply_keyboard

bot = Bot(token=TOKEN)
default = DefaultBotProperties(parse_mode=ParseMode.HTML)
dp = Dispatcher()
fastfoodlar = ['1. Hot dog 12000\n', '2. Gamburger 20000\n', '3. Misnoy hot dog 15000\n', '4. Lavash T.G, M.G 22000\n',
               '5. Cheeseburger 20000\n']
user_date = {}


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Ish botiga xush kelibsiz! VAriantlarni tanlang:', reply_markup=main_keyboard)

    user_date[message.from_user.id] = {}


@dp.message(F.text.contains("Bo'sh ish o\'rinlari"))
async def fastfood_handler(message: types.Message):
    await message.answer("Mana bizning hozirgi bo'sh ish o'rinlarimiz:", reply_markup=vacancies_keyboard)


@dp.message(F.text.in_(vacancies))
async def vacancies_handler(message: types.Message):
    vacancy = message.text
    description = vacancies[vacancy]
    user_date[message.from_user.id]['vacancy'] = vacancy
    await message.answer(f"{vacancy}: {description}\n\n Ushbu lovzimga ariza borishni xohlaysizmi?",
                         reply_markup=apply_keyboard)


@dp.message(F.text.in_(["Yes", "No"]))
async def apply_keyboard(message: types.Message):
    if message.text == "No":
        user_date[message.from_user.id]['vacancy'] = ""
    await message.answer("Ajoyib! Ismingiz nima? (example name:'your_phone'")


@dp.message(F.text.startwith("name"))
async def save_name(message: types.Message):
    if message.text not in user_date[message.from_user.id]:
        name = message.text.split(':')[1]
        user_date[message.from_user_id]['name'] = name
        print(user_date)
        await message.answer("Rahmat! Telefon raqamini kiriting: (example phone:'your_phone')")


@dp.message(F.text.startwith("phone"))
async def save_phone(message: types.Message):
    if message.text not in user_date[message.from_user.id]:
        phone = message.text.split(':')[1]
        user_date[message.from_user.id]['phone'] = phone
    await message.answer("Rahmat! Kasbingiz nima? (example job:'your_job')")
    print(user_date)


@dp.message(F.text.startwith("job"))
async def save_job(message: types.Message):
    if message.text not in user_date[message.from_user.id]:
        job = message.text.split(':')[1]
        user_date[message.from_user.id]['job'] = job
    await message.answer("Rahmat! Necha yillik tajribangiz bor? 9example exerience:'your_exerience'")


@dp.message(F.text.startwith("experience"))
async def save_experience(message: types.Message):
    if message.text not in user_date[message.from_user.id]:
        experience = message.text.split(':')[1]
        user_date[message.from_user.id]['experience'] = experience
        await message.answer("Rahmat! Iltimos, malakalaringizni qisqacha tavsiflab bering.")
        await message.answer("example description: 'your_qualification'")


@dp.message(F.text.startwith("description"))
async def save_description(message: types.Message):
    if message.text not in user_date[message.from_user.id]:
        description = message.text.split(':')[1]
        user_date[message.from_user.id]['description'] = description
    await message.answer("Rahmat! Sizning arizangiz topshirildi.", reply_markup=main_keyboard)
    print(user_date)


@dp.message(F.text == "Mening malumotlarim")
async def get_my_info(message: types.Message):
    info = user_date.get(message.from_user.id, {})
    name = info.get('name', 'topilmadi')
    phone = info.get('name', 'topilmadi')
    occupation = info.get('occupation', 'topilmadi')
    experience = info.get('exerience', 'topilmadi')

    await message.answer(
        f"Your information:\n\nName: {name}\nPhone: {phone}\nOccupation: {occupation}\nExperience: {experience}",
        reply_markup=main_keyboard)

async def main():
    print("Ishlayapti...")
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())