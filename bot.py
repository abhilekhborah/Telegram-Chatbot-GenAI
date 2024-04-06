from aiogram import Bot, Dispatcher
from aiogram import types, executor
from dotenv import load_dotenv
import os
import logging



load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi\nI am a Chat Bot! Created by Abhilekh. How can i assist you?")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm a bot created by Abhilekh! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)

@dispatcher.message_handler()
async def echo_all(message: types.Message):
    """
    A handler to echo all incoming messages.

    Args:
    message (types.Message): _description_
    """
    await message.reply(message.text)

if __name__ ==  "__main__":
    executor.start_polling(dispatcher, skip_updates=True)