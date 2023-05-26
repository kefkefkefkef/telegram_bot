import os
import logging
import pandas as pd
from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler()
async def translit(message: types.Message):
    translit_csv = pd.read_csv('translit.csv')
    
    new_string = 'VERONIKA, '
    for x in message.text:
        if x.upper() in translit_csv['Национальный знак'].to_list():
            new_string += translit_csv['Рекомендуемая транслитерация'].to_list()[translit_csv['Национальный знак'].to_list().index(x.upper())]
        else:
            new_string += x
    
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await bot.send_message(user_id, new_string)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Helllo, {user_name}!'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

# @dp.message_handler()
# async def send_welcome(message: types.Message):
#     user_name = message.from_user.full_name
#     user_id = message.from_user.id
#     text = message.text
#     logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
#     await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)