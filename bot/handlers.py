from main import bot, dp
from aiogram.types import Message
from config import admin_id


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')


@dp.message_handler()
async def echo(message: Message):
    text = f'Привет, ты отправил - {message.text}'
    await message.answer(text=text)