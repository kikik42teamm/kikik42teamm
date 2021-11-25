from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

banned_users = set()

user_data = {}


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, '{0.first_name}'.format(message.from_user))

@dp.message_handler(commands="button")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["", "", "", "", ""]
    keyboard.add(*buttons)
    await message.answer("", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text =="")
async def with_puree(message: types.Message):
    await message.reply("")

@dp.message_handler(lambda message: message.text == "")
async def without_puree(message: types.Message):
    await message.reply("")

@dp.message_handler(lambda message: message.text == "Погода")
async def without_puree(message: types.Message):
    await message.reply("")

@dp.message_handler(lambda message: message.text == "")
async def without_puree(message: types.Message):
    await message.reply("")

@dp.message_handler(lambda message: message.text == "0")
async def without_puree(msg: types.Message):
    print(f"{msg.from_user.full_name} пишет, но мы ему не ответим!")
    return True

@dp.message_handler(lambda message: message.text == "ban - только для админа группы", user_id=) 
async def handle_ban_command(msg: types.Message):
    try:
        abuser_id = int(msg.get_args())
    except (ValueError, TypeError):
        return await msg.reply("Укажи ID пользователя.")
    
    banned_users.add(abuser_id)
    await msg.reply(f"Пользователь {abuser_id} заблокирован.")

@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joned(message: types.Message):
   print("JOIN message removed")
   await message.delete()

@dp.message_handler()
async def filter_message(message: types.Message):
   if '' in message.text:
      await message.delete()

   if '' in message.text:
      await message.delete()

   if '' in message.text:
      await message.delete()

   if '' in message.text:
      await message.delete()

   if '' in message.text:
      await message.delete()

   if '' in message.text:
      await message.delete()

   if '' in message.text:
      await message.delete()
    
   if '' in message.text:
      await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp)
