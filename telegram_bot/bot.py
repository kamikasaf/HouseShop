import logging
from db_bot import BD1
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token='5421046604:AAE-2owktJ78RHaUeBMkHc0kUXfuzqlN3ys')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Здравствуйте  {message.from_user.first_name},  {message.from_user.last_name},  используйте  коману  /listButtons  чтобы  узнать  что  я  умею")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)



@dp.message_handler(commands=['Список_Продуктов'])
async def product(message: types.Message):
    await message.reply(BD1.product())


@dp.message_handler(commands='Ссылка_на_список_продуктов')
async def links(message: types.Message):
    from aiogram.utils.markdown import link
    text = link('productsHouseshop', 'https://houseshop.herokuapp.com/products/')
    await message.reply(text)


@dp.message_handler(commands=["listButtons"])
async def buttons(message: types.Message):
    item1=KeyboardButton("Список_Продуктов")
    item2=KeyboardButton('Ссылка_на_список_продуктов')
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(item1, item2)
    await message.reply('Кнопки', reply_markup=markup)


@dp.message_handler(content_types="text")
async def buttons(message):
    if message.text == "Список_Продуктов":
        await product(message)
    elif message.text == "Ссылка_на_список_продуктов":
        await links(message)
    else:
        await bot.send_message(message.chat.id, "я не понял что вы имели ввиду,  используйте  коману  /listButtons  чтобы  узнать  что  я  умею")


if __name__ == '__main__':
    executor.start_polling(dp)
