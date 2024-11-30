from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Добавить запись"))
    keyboard.add(KeyboardButton("Просмотреть записи"))
    keyboard.add(KeyboardButton("Редактировать запись"))
    keyboard.add(KeyboardButton("Удалить запись"))
    return keyboard