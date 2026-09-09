import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

# Главная клавиатура
def get_main_keyboard():
    kb = [
        [KeyboardButton(text="🎓 Обучение"), KeyboardButton(text="❓ Задать вопрос по товару")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Клавиатура категорий обучения
def get_categories_keyboard():
    inline_keyboard = [
        [InlineKeyboardButton(text="📁 Профиль", callback_data="cat_profile")],
        [InlineKeyboardButton(text="📁 Фурнитура", callback_data="cat_hardware")],
        [InlineKeyboardButton(text="📁 Станки", callback_data="cat_machines")],
        [InlineKeyboardButton(text="📁 Битрикс24", callback_data="cat_bitrix")],
        [InlineKeyboardButton(text="📁 1С", callback_data="cat_1c")],
        [InlineKeyboardButton(text="📁 Профстрой", callback_data="cat_profstroy")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"Здравствуйте, {message.from_user.first_name}!\n\n"
        f"Добро пожаловать в обучающий бот отдела продаж.\n"
        f"Выберите интересующий вас раздел:"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@dp.message(F.text == "🎓 Обучение")
async def show_learning_categories(message: Message):
    await message.answer("Выберите раздел обучения:", reply_markup=get_categories_keyboard())

@dp.message(F.text == "❓ Задать вопрос по товару")
async def ask_product_question(message: Message):
    await message.answer("Напишите ваш вопрос по товару или характеристикам, и я постараюсь помочь!")

async def main():
    if not BOT_TOKEN:
        print("ОШИБКА: Токен бота не найден в переменных окружения!")
        return
    bot = Bot(token=BOT_TOKEN)
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
