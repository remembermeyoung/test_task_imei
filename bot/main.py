from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
from imei_request import imei_request

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text.regexp(r'^[0-9]{15}$'))
def imei_handler(message: Message):
    if user in white_list:
        imei_request(message.text, API_TOKEN)
        return message.reply(response)
    else:
        pass


@dp.message(lambda message: True)
async def dont_understand(message):
    if message.text is not None:
        await message.answer(text=dont_understand_message)





