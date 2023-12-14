import logging
import asyncio
import os

from aiogram import Bot, Dispatcher,  types 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()

api_token = os.environ.get("ECHOBOT_API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api_token)
dp = Dispatcher()

def make_keyboard():
    """
    Oпределяет функцию make_keyboard, которая создает разметку
    встроенной клавиатуры с одной кнопкой под сообщением.
    """
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ссылка на код бота", url="https://github.com/dima2040/tgbot"),]
        ]
    )
    return markup

def make_replaykeyboard():
    """
    Oпределяет функцию, которая создает разметку
    встроенной клавиатуры с четырьмя кнопками в две строчку внизу экрана.
    """
    markup = ReplyKeyboardMarkup( 
        keyboard=[
            [
                KeyboardButton(text="кнопка 1_1"), 
                KeyboardButton(text="кнопка 1_2")
            ]
        ]
    )
    return markup


def make_many_buttons_replaykeyboard():
    """
    Oпределяет функцию, которая создает разметку
    встроенной клавиатуры с несколькими рядами по 12 кнопок.
    """
    markup = ReplyKeyboardMarkup( 
        keyboard=[
            [
                KeyboardButton(text="🟧") for _ in range(12)
            ],
            [
                KeyboardButton(text="🟥") for _ in range(12)
            ],
            [
                KeyboardButton(text="🟪") for _ in range(12)
            ],
            [
                KeyboardButton(text="🟩") for _ in range(12)
            ],
        ]
    )
    return markup


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
     """Посылает приветственное сообщение"""
     await message.reply("✌️ Привет это echobot!", reply_markup=make_keyboard())

@dp.message(Command("help"))
async def send_help(message: types.Message):
    """Отправляет сообщение справки"""
    help_message = """
    📝 Это сообщение справки echobot. Вот доступные команды:\n\n
    /start - Запустить бота\n
    /buttons - Показать пример кнопок \n
    /help - Показать это сообщение справки\n
    *** - Любая другая фараза или команда будет отправлены в ответ в том же виде 
    """
    await message.reply(help_message, reply_markup=make_replaykeyboard())

@dp.message(Command("buttons"))
async def send_help(message: types.Message):
    """Отправляет сообщение с кнопкам"""
    await message.reply("💪Много кнопок!", reply_markup=make_many_buttons_replaykeyboard())


@dp.message()
async def echo_handler(message: types.message):
    """Отправляет копию полученного сообщения обратно в тот же чат."""
    await message.send_copy(chat_id=message.chat.id)


async def main():
    """Запустите опрос обновлений от Telegram-бота с помощью библиотеки aiogram."""
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
