import asyncio 
import logging 
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command 
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


from config_reader import config
from weather import weather, osadki, temperature
from date import date
from correct_cities import replacitinator



logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
    await message.answer("Привет! Я МетеоБот, напишите название своего города или отправьте мне команду /cities, чтобы выбрать город из перечня")

@dp.message(Command("info")) 
async def cmd_start(message: types.Message): 
    await message.answer("Это МетеоБот, написанный на языке программирования Python c помощью библиотеки aiogram учеником 10 Д класса ГБОУ школы 1279 ”Эврика” Шевченко Андреем под руководством Доминика Анри Миссанда Нгурума. Бот создан в качестве индивидуального проекта, a так же для дальнейшего развития")

@dp.message(Command('cities'))
async def cities(message: types.Message, bot = Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Москва", callback_data="moskva"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Санкт-Петербург", callback_data="sankt_peterburg"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Красноярск", callback_data="krasnoyarsk"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Нижний Новгород", callback_data="nizhniy_novgorod"
    ))
    
    builder.adjust(2)
    await message.answer(
        "Выберите город из перечня:", 
        reply_markup=builder.as_markup()
    )



@dp.callback_query(F.data == "moskva")
async def msk(callback: types.CallbackQuery):
    global city
    city = 'moskva'
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
        text=date(i), callback_data=f"pogoda{i}"
    ))
        builder.adjust(1)
    await callback.answer(text="Москва") 
    await callback.message.answer(
        "Выберите дату прогноза погоды для города Москва: ", 
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "sankt_peterburg")
async def msk(callback: types.CallbackQuery):
    global city
    city = 'sankt_peterburg'
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
        text=date(i), callback_data=f"pogoda{i}"
    ))
        builder.adjust(1)
    await callback.answer(text="Санкт-Петербург") 
    await callback.message.answer(
        "Выберите дату прогноза погоды для города Санкт-Петербург: ", 
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "krasnoyarsk")
async def msk(callback: types.CallbackQuery):
    global city
    city = 'krasnoyarsk'
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
        text=date(i), callback_data=f"pogoda{i}"
    ))
        builder.adjust(1)
    await callback.answer(text="Красноярск") 
    await callback.message.answer(
        "Выберите дату пргноза погоды для города Красноярск: ", 
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "nizhniy_novgorod")
async def msk(callback: types.CallbackQuery):
    global city
    city = 'nizhniy_novgorod'
    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
        text=date(i), callback_data=f"pogoda{i}"
    ))
        builder.adjust(1)
    await callback.answer(text="Нижний Новгород") 
    await callback.message.answer(
        "Выберите дату прогноза погоды для города Нижний Новгород: ", 
        reply_markup=builder.as_markup()
    )




@dp.message(F.text)
async def pogodka(message: types.Message, bot = Bot):
    global city
    city = replacitinator(message.text)
    city_in_answer = message.text

    if not weather(city) or not temperature(city) or not osadki(city):
        await message.answer("Попробуйте написать город в другой форме")
        return

    builder = InlineKeyboardBuilder()
    for i in range(1, 8):
        builder.add(types.InlineKeyboardButton(
        text=date(i), callback_data=f"pogoda{i}"        
    ))
        builder.adjust(1)
    await message.answer(
        f"Выберите дату прогноза погоды для города {city_in_answer.title ()}: ", 
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data.startswith("pogoda"))
async def send_weather(callback: types.CallbackQuery):
    day_index = int(callback.data[-1])  
    await callback.message.answer(date(day_index))  
    start_index = (day_index - 1) * 4  
    await callback.message.answer("ночь: " + weather(city)[start_index] + ", " + temperature(city)[start_index] + ", осадки: " + osadki(city)[start_index])
    await callback.message.answer("утро: " + weather(city)[start_index + 1] + ", " + temperature(city)[start_index+1] + ", осадки: " + osadki(city)[start_index+1])
    await callback.message.answer("день: " + weather(city)[start_index + 2] + ", " + temperature(city)[start_index+2] + ", осадки: " + osadki(city)[start_index+2])
    await callback.message.answer("вечер: " + weather(city)[start_index + 3] + ", " + temperature(city)[start_index+3] + ", осадки: " + osadki(city)[start_index+3])


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




     
