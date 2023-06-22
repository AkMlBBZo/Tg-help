from aiogram import Bot, types
from config import *
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time
import os

os.system("cls")

bot = Bot(token=BOT_TOKEN)
dp  = Dispatcher(bot)


@dp.message_handler(content_types=["text", "sticker", "photo", "voice", "document"])
async def content_handler(message: types.Message):
    if(message.chat.id==USER_ID and message.chat.type == 'private'):
        try:
            if message.content_type == "sticker":
                await bot.send_sticker(chat_id=OUTPUT_ID, sticker=message.sticker["file_id"])
            elif message.content_type == "photo":
                await bot.send_photo(chat_id=OUTPUT_ID,photo=message.photo[-1].file_id,caption=message.caption)
            elif message.content_type == "voice":
                await bot.send_voice(chat_id=OUTPUT_ID, voice=message.voice["file_id"])
            elif message.content_type == "document":
                await bot.send_document(chat_id=OUTPUT_ID,document=message.document["file_id"],caption=message.caption)
            else:
                await bot.send_message(text=message.text, chat_id=OUTPUT_ID)
        except:
                print('-2' + '\n'*2)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
