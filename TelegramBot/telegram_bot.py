from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5860668091:AAFqomKS75OAQ9ST27fbCTK1tsg2Bj78WUc'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ бот от Электрон Сервис!")
 
@dp.message_handler()
async def echo(message: types.Message):
   
   
   
   
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)