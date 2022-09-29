from tkinter import W
from aiogram import *
from aiogram.types import *
import keyboards as kb


bot = Bot(token='5466165678:AAG9PT3lDFVa71vSuI8--uKMRpkQMNLNQO4')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def keyboard(message: types):
    await message.answer('Button', reply_markup=kb.start)
    await message.answer('Button', reply_markup=kb.button1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
