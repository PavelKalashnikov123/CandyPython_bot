# юда все функции отправляющие сообщения


from aiogram import types

from bot import bot
import model
import commands


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. \n'
                           f'Ваш противник МЕГАБОТ - первый ход обределяется жеребьевкой /lot')


async def end (message: types.Message):
    if model.winner == 1:
        await bot.send_message(message.from_user.id,
                            f'Ну и вали, жадина!')
    else:
        await bot.send_message(message.from_user.id,
                            f' До свидания, {message.from_user.first_name}!')


async def lotResult (message: types.Message):
    if model.lot == 1:
        await bot.send_message(message.from_user.id,
                        f' Первым ходит {message.from_user.first_name}')
    else:
        await bot.send_message(message.from_user.id,
                        f' Первым ходит МЕГАБОТ')
        await bot.send_message(message.from_user.id,
                        f'  5 - у тебя нет шансов, кусок мяса! ')

async def showTotal (message: types.Message):
        await bot.send_message(message.from_user.id,
                        f' Осталось {model.count} конфет')

async def showBotSteep (message: types.Message):
        await bot.send_message(message.from_user.id,
                        f'{commands.steepBot}')

async def showWinner (message: types.Message):
    if model.winner == 1:
        await bot.send_message(message.from_user.id,
                        f' Победитель {message.from_user.first_name}\n'
                        f' Хотите сыграть еще - нажмите /lot \n'
                        f' Уйти и не поделиться /finish ')
    else:
        await bot.send_message(message.from_user.id,
                        f' Победитель МЕГАБОТ \n'
                        f' Хотите продуть еще - нажмите /lot \n'
                        f' Уйти и остаться без сладкого /finish ')

async def wrongNumber (message: types.Message):
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')

async def wrongText (message: types.Message):
        await bot.send_message(message.from_user.id, 'Эх...')