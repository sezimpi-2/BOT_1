from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


survey_router = Router()

class RestoranSurvey(StatesGroup):
    name = State() # name - имя пользователя
    date= State() # дата
    instagram = State() # - instagram пользователя
    meals= State() #- любимый вид еды
    purity = State() # чистота заведения

@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(RestoranSurvey.name)
    await message.answer("Как вас зовут?")

@survey_router.message(RestoranSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    message.answer(f"Начнем , {name}!")
    await state.set_state(RestoranSurvey.date)
    await message.answer("Введите дату посещения?")

@survey_router.message(RestoranSurvey.date)
async def process_age(message: types.Message, state: FSMContext):
    date = message.text
    if not date.isdigit():
        await message.answer("Пожалуйста, введите число")
    await state.set_state(RestoranSurvey.instagram)
    await message.answer("Ваш instagram аккаунт?")

@survey_router.message(RestoranSurvey.instagram)
async def process_gender(message: types.Message, state: FSMContext):
    instagram = message.text
    await state.update_data(instagram=instagram)
    await state.set_state(RestoranSurvey.meals)
    await message.answer("Ваша любимая еда?")

@survey_router.message(RestoranSurvey.meals)
async def process_genre(message: types.Message, state: FSMContext):
    meals = message.text

    await state.update_data(meals=meals)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="отлично")],
            [types.KeyboardButton(text="хорошо")],
            [types.KeyboardButton(text="плохо")]
        ],
        resize_keyboard=True
    )
    await state.set_state(RestoranSurvey.purity)
    await message.answer("Как вы оцениваете чистоту нашего заведения?", reply_markup=kb)

purity_assessment = ["плохо", "хорошо", "отлично"]

@survey_router.message(RestoranSurvey.purity, F.text.lower().in_(purity_assessment))
async def process_rating(message: types.Message, state: FSMContext):
    purity = message.text
    purity = purity_assessment.index(purity) + 3
    await state.update_data(purity=purity)
    await message.answer("Спасибо за прохождение опроса😊\nМы будем рады встретить вас в нашем заведении ещё раз!💖")
    await state.clear()