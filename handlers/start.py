from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.main_menu import get_main_menu_keyboard
from database.db_session import Session
from models import User


class StartState(StatesGroup):
    waiting_for_start = State()


async def start_command(message: types.Message, state: FSMContext):
    session = Session()
    user = session.query(User).filter(User.telegram_id == message.from_user.id).first()
    if not user:
        user = User(telegram_id=message.from_user.id)
        session.add(user)
        session.commit()

    await message.answer(
        "Привет! Я твой личный бот-записная книжкуа.",
        reply_markup=get_main_menu_keyboard(),
    )
    await state.finish()
