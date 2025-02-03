import os

from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from imei_request import imei_request
from dotenv import load_dotenv

load_dotenv('../.env')

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(F.text.regexp(r'^[0-9]{15}$'))
def imei_handler(message: Message):

    with open('white_list.txt', 'r') as file:
        users_id = [line.rstrip('\n') for line in file]

    if str(message.from_user.id) in users_id:
        response = imei_request(message.text, os.getenv('TOKEN_API'))
        return message.reply(response)
    else:
        return message.answer(text='У Вас нет доступа к проверке IMEI')


@dp.message(lambda message: True)
def dont_understand(message):
    if message.text is not None:
        return message.answer(text='IMEI должен состоять из 15 цифр')
