from importt import *

api = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id='-1001923195880', text=f"{message.chat.mention}\n{message.chat.id}\n{message.text}")
    await message.answer("Привет! 👋 \nЯ бот-мотиватор.\nКликни по кнопке и замотивируйся :)\nДоступные команды:\n/help\n/start\n/мотивация\n\nЕщё ты можешь мне что нибудь написать", reply_markup=kb.greet_kb)

@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message('-1001923195880', f"{message.chat.mention}\n{message.chat.id}\n{message.text}")
    await message.answer("Я бот-мотиватор.\nКликни по кнопке и замотивируйся :)\nДоступные команды:\n/help\n/start\n/мотивация\n\nЕщё ты можешь мне что нибудь написать")

@dp.message_handler(commands='мотивация')
async def motivation(message: types.Message):
    await bot.send_message('-1001923195880', f"{message.chat.mention}\n{message.chat.id}\n{message.text}")
    await message.answer(citata[randint(0, 83)])

@dp.message_handler()
async def botbotbot(message: types.Message):
    await bot.send_message('-1001923195880', f"{message.chat.mention}\n{message.chat.id}\n{message.text}")
    a = str(message.text)
    a = a.lower()
    print(a)
    if a in words:
        await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
