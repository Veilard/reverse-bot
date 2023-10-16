from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '6529821039:AAGoFUYXVISAPXZ5t8Xm6lYtJrmHO9NifLg'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я инвертирую твои сообщения.")

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("Зачем тебе помощь? Просто напиши что-нибудь.")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text[::-1])
    print(msg)

if __name__ == '__main__':
    print('Polling...')
    executor.start_polling(dp)
