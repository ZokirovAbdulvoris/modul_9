from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

vacancies = {
    'Software Engineer': "Biz Python va JavaScript-da 3+ yillik tajribaga ega dasturiy ta'minot muhandisini qidirmoqdamiz.",
    'Data Analyst': "Biz SQL va ma'lumotlarni vizualizatsiya vositalarida tajribaga ega bo'lgan ma'lumotlar tahlilchisini qidirmoqdamiz.",
    'Product Manager': "Biz tezkor ishlab chiqish metodologiyalarida tajribaga ega mahsulot menejerini qidirmoqdamiz.",
    'UX Designer': "Biz foydalanuvchilarni tadqiq qilish va telfreymlash bo'yicha tajribaga ega UX dizaynerini qidirmoqdamiz.",
    'Marketing Manager': "Biz raqamli marketing va SEO bo'yicha tajribaga ega marketing menejerini qidirmoqdamiz.",
    'Sales Representative': "Biz B2B savdo va CRM dasturiy ta'minotida tajribaga ega bo'lgan savdo vakilini qidirmoqdamiz."
}

main_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
main_keyboard.keyboard.append([KeyboardButton(text="Bo'sh ish o'rinlari"), KeyboardButton(text="Mening ma'lumotlarim")])
main_keyboard.keyboard.append([KeyboardButton(text="Sozlamalar"), KeyboardButton(text="Biz bilan bog'lanish")])

vacancies_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
for vacancy in vacancies:
    vacancies_keyboard.keyboard.append([KeyboardButton(text=vacancy)])
vacancies_keyboard.keyboard.append([KeyboardButton(text='Back')])

apply_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
apply_keyboard.keyboard.append([KeyboardButton(text='Yes'), KeyboardButton(text='No')])
