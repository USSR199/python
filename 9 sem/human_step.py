from aiogram.types import Message
import keyboards


async def human_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, твой ход! '
                         f'Сколько конфет ты хочешь забрать со стола?', reply_markup=keyboards.kb_step)
