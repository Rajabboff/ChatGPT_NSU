import logging
import openai
import os
from aiogram import Bot, Dispatcher, types, executor

# Bu yerdagi BOT_TOKEN o'zgartiriladi
BOT_TOKEN = '6262013126:AAExPZIT9WipYYivF6VbsDPhf191-IX_LUE'
openai.api_key ='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'

# Logging konfiguratsiyasi
logging.basicConfig(level=logging.INFO)

# Botni yaratish
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# OpenAI API so'rovnoma maxsulotini aniqlash

# /start komandasi uchun funksiya yaratish
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Salom, men sizning savollarga javob beruvchi botman. \n ' belgisidan foydalanmang" )


# Sizning boshqa savollariga javob berish uchun funksiya yaratish
@dp.message_handler()
async def generate_answer(message: types.Message):
    # Foydalanuvchi habar matnini olish
    input_text = message.text

    # OpenAI API dan javob olish
    response = openai.Completion.create(prompt = input_text, model="text-davinci-003", temperature = 0.6,  max_tokens=1000)

    # Javobni chiqarish
    await message.answer(response.choices[0].text)

if __name__ == '__main__':
    # Long polling orqali botni ishga tushiramiz
    executor.start_polling(dp, skip_updates=True)