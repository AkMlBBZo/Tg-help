from pyrogram import Client, filters
from config import *
from os import system

system('start cmd.exe /k python "aiogram_part.py"')

system("cls")

api_id=API_ID
api_hash=API_HASH

app = Client("my_account",api_id,api_hash)

app.start()

app.stop()



print("Bot_started")



@app.on_message()
async def echo(client, message):
    if(message.chat.id==IMPORT_ID):
        try:
            if message.sticker:
                await app.send_sticker(chat_id=BOT_ID, sticker=message.sticker.file_id)
            elif message.photo:
                await app.send_photo(chat_id=BOT_ID,photo=message.photo.file_id,caption=message.caption)
            elif message.audio:
                await app.send_audio(chat_id=BOT_ID, audio=message.audio.file_id)
            elif message.document:
                await app.send_document(chat_id=BOT_ID,document=message.document.file_id,caption=message.caption)
            else:
                await app.send_message(chat_id=BOT_ID, text=message.text)
        except:
            print("-1" + "\n" * 2)

app.run()