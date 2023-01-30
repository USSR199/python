import data
import keyboards


async def who_is_win(message, taken_candies: int, player: str):
    if data.get_total() <= 0:
        if player == 'human':
            await message.answer(f'{message.from_user.first_name} взял(а) {taken_candies} конфет(у/ы).\n'
                                 f'Победил(а) {message.from_user.first_name}!', reply_markup=keyboards.kb_end)
        else:
            await message.answer(f'Победил PC!', reply_markup=keyboards.kb_end)
        data.start_new_game()
        return True
    else:
        return False
