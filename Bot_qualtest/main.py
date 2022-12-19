from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


HELP_COMMAND = """
/help - список команд
/start - начало работы
"""

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Привет')
    await message.delete()




if __name__ == '__main__':
    executor.start_polling(dp)