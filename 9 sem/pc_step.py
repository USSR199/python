from aiogram.types import Message
import data
import random
import human_step
import check_winner
import keyboards


async def pc_turn(message):
    total = data.get_total()
    if total <= 28:
        taken_candies = total
    else:
        if data.get_bot_level() == 1:
            taken_candies = random.randint(1, 28)
        else:
            if total % 29 > 0:
                taken_candies = total % 29
            else:
                taken_candies = random.randint(1, 28)
    data.take_candies(taken_candies)
    await message.answer(f'РC взял {taken_candies} конфет(у/ы).\n'
                         f'На столе осталось {data.get_total()} конфет(у/ы).', reply_markup=keyboards.kb_step)
    if await check_winner.who_is_win(message, taken_candies, 'PC'):
        return
    await human_step.human_turn(message)
