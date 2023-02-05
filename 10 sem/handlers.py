from aiogram import types
from loader import dp
from random import randint
max_count = 150
max_candy = 28
total = 0
new_game = False
duel = []
first_move = 0
current = 0
photo = None

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    global photo
    name = message.from_user.first_name
    await message.answer(f'Привет {name} , если хочешь поиграть c ботом, отправь сообщение : \n'
                         '/new_game \n'
                         'Чтобы играть против другого игрока ,напиши сообщение \n'
                         '/player1 .\n '
                         'Чтобы узнать условия игры отправь сообщение : /rules ')
    with open('/Users/alexey/Desktop/Python/123.jpeg', 'rb') as photo:
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(commands=['rules'])
async def mes_rules(message: types.Message):
    global max_count
    global max_candy
    total = max_count
    await message.answer('Правила игры в конфеты :\n'
                         f'На столе лежит {total} конфет,\n'
                         f'за один раз можно взять максимум {max_candy} конфет ,\n'
                         'первым ходит игрок выбранный случайным образом \n'
                         'Выигрывает игрок ,который заберёт последние конфеты,\n'
                         'не нарушая правила ( то есть брать не менее 1 и не более договорённого кол-ва')
    await message.answer('Для настройки общего колличества конфет на столе и максимального кол-ва конфет,\n'
                         'которое можно взять за один раз напиши в сообщении : /set и кол-во конфет в цифрах через пробел \n'
                         'Пример : /set 200 32 - где 200 - общее кол-во конфет , 32 - кол-во конфет , которое можно взять за один раз'
                         'Напиши в сообщении /start , чтобы вернуться в меню ')


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global duel
    global total
    global new_game
    global max_count
    global first_move
    total = max_count
    new_game = True
    duel = []
    first_move = randint(0, 1)
    if first_move:
        await message.answer(f'Игра началась. Первым ходит {message.from_user.first_name} \n'
                             f'На столе {total} конфет. Максимум можно взять {max_candy} конфет')
        with open('/Users/alexey/Desktop/Python/1639508722_5-sportishka-com-p-khodi-v-shakhmatakh-krasivo-foto-6.jpg', 'rb') as photo:
            await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)
    else:
        await message.answer(f'Игра началась. Первым ходит Ботяра ')
        with open('/Users/alexey/Desktop/Python/1616699300_58-p-zhdun-krasivo-61.jpg', 'rb') as photo:
            await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)
        await bot_turn(message)


@dp.message_handler(commands=['player1'])
async def mes_duel(message: types.Message):
    global duel
    duel=[]
    duel.append(int(message.from_user.id))
    await message.answer(f'{message.from_user.first_name} , ждите второго игрока ')
    print(duel)
    return duel


@dp.message_handler(commands=['player2'])
async def mes_duel(message: types.Message):
    global max_candy
    global total
    global new_game
    global max_count
    global duel
    global first_move
    total = max_count
    global current
    global photo
    # name = message.from_user.first_name
    duel.append(int(message.from_user.id))
    # duel.append(int(message.text.split()[1]))
    first_move = randint(0, 1)
    if len(duel) > 1:
        if first_move:
            await dp.bot.send_message(duel[0], f'Твой ход первый . На столе {total} конфет\n'
                                      f'Максимум можно взять {max_candy} конфет')
            with open('/Users/alexey/Desktop/Python/1639508722_5-sportishka-com-p-khodi-v-shakhmatakh-krasivo-foto-6.jpg', 'rb') as photo:
                await dp.bot.send_photo(chat_id=duel[0], photo=photo)
            await dp.bot.send_message(duel[1], 'Ходит соперник , жди своего хода\n'
                                      f'На столе {total} конфет. Максимум можно взять {max_candy} конфет')
            with open('/Users/alexey/Desktop/Python/1616699300_58-p-zhdun-krasivo-61.jpg', 'rb') as photo:
                await dp.bot.send_photo(chat_id=duel[1], photo=photo)
        else:
            await dp.bot.send_message(duel[1], f'Твой ход первый . На столе {total} конфет\n'
                                      f'Максимум можно взять {max_candy} конфет')
            with open('/Users/alexey/Desktop/Python/1639508722_5-sportishka-com-p-khodi-v-shakhmatakh-krasivo-foto-6.jpg', 'rb') as photo:
                await dp.bot.send_photo(chat_id=duel[1], photo=photo)
            await dp.bot.send_message(duel[0], 'Ходит соперник , жди своего хода\n'
                                      f'На столе {total} конфет. Максимум можно взять {max_candy} конфет')
            with open('/Users/alexey/Desktop/Python/1616699300_58-p-zhdun-krasivo-61.jpg', 'rb') as photo:
                await dp.bot.send_photo(chat_id=duel[0], photo=photo)
        new_game = True
        current = duel[0] if first_move else duel[1]
    


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    global max_candy
    global photo
    name = message.from_user.first_name

    if not new_game:
        # if len(message.text.split()) == 1:
        #     await message.answer(f'{name} введите кол-во конфет после команды /set ')
        if len(message.text.split()) > 1:
            count = message.text.split()[1]
        if len(message.text.split()) > 2:
            max_candy = message.text.split()[2]
            if count.isdigit() and max_candy.isdigit():
                max_count = int(count)
                max_candy = int(max_candy)
                await message.answer(f'Конфет теперь {max_count} штук .\n За один раз можно взять максимум {max_candy} конфет\n '
                                     'Чтобы вернуться к выбору игры , напиши /start ')
            else:
                await message.answer(f'{name} , смотри внимательнее , что ты пишешь')
                with open('/Users/alexey/Desktop/Python/1399_900.jpg', 'rb') as photo:
                    await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)

        elif len(message.text.split()) > 1 and count.isdigit():
            max_count = int(count)
            await message.answer(f'Конфет теперь {max_count} штук .\n '
                                 'Чтобы вернуться к выбору игры , напиши /start ')
        else:
            await message.answer(f'{name} , смотри внимательнее , что ты пишешь')
            with open('/Users/alexey/Desktop/Python/1399_900.jpg', 'rb') as photo:
                await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)

    else:
        await message.answer(f'{name} , нельзя менять правила во время игры  ')


@dp.message_handler()
async def mes_take_candy(message: types.Message):
    global total
    global new_game
    global max_candy
    global max_count
    global duel
    global first_move
    global current
    name = message.from_user.first_name
    count = message.text
    if len(duel) == 0:
        if new_game:
            if message.text.isdigit() and 0 < int(message.text) < max_candy+1:
                total -= int(message.text)
                if total <= 0:
                    await message.answer(f'УРРРААА {name} ты победил \n')
                    with open('/Users/alexey/Desktop/Python/aec61ac0e54c1cd6c13538e55bbcbb48.jpg', 'rb') as photo:
                        await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)
                    await message.answer(f'Если хочешь продолжить играть напиши :  /start \n'
                                         'Если хочешь поменять условия игры,отправь сообщение /set и кол-во конфет через пробел ')
                    new_game = False
                else:
                    await message.answer(f'{name} взял  {message.text} конфет '
                                         f' на столе осталось {total}')
                    await bot_turn(message)
            else:
                await message.answer(f'{name} возьмите от 1 до {max_candy} конфет')
    else:
        if current == int(message.from_user.id):
            name = message.from_user.first_name
            count = message.text
            if new_game:
                if message.text.isdigit() and 0 < int(message.text) < max_candy+1:
                    total -= int(message.text)
                    if total <= 0:
                        await message.answer(f'УРРРААА {name} ты победил(а) \n')
                        with open('/Users/alexey/Desktop/Python/aec61ac0e54c1cd6c13538e55bbcbb48.jpg', 'rb') as photo:
                            await dp.bot.send_photo(chat_id=message.from_id, photo=photo)

                        await dp.bot.send_message((enemy_id()), 'К сожалению ты проиграл(а). Очень жаль )))\n'
                                                  f'Если хочешь продолжить играть напиши :  /start \n'
                                                  'Если хочешь поменять условия игры,отправь сообщение \n'
                                                  '/set \n'
                                                  'и кол-во конфет через пробел ')
                        with open('/Users/alexey/Desktop/Python/i.jpeg', 'rb') as photo:
                            await dp.bot.send_photo(chat_id=enemy_id(), photo=photo)
                        await message.answer(f'Если хочешь продолжить играть напиши :  /start \n'
                                             'Если хочешь поменять условия игры,отправь сообщение \n'
                                             '/set \n'
                                             'и кол-во конфет через пробел ')
                        new_game = False
                    else:
                        await message.answer(f'Вы взяли  {message.text} конфет '
                                             f' на столе осталось {total}')
                        await dp.bot.send_message((enemy_id()), f'{name} взяла(а) {message.text} конфет')
                        await dp.bot.send_message((enemy_id()), f'На столе осталось {total} конфет\n'
                                                  'Теперь твой ход , бери конфеты.\n')
                        swith_player()
                else:
                    await message.answer(f'{name} возьмите от 1 до {max_candy} конфет')


async def bot_turn(message: types.Message):
    global total
    global new_game
    global max
    bot_take = 0
    if 0 < total < max_candy+1:
        bot_take = total
        total -= bot_take
        await message.answer(f'Бот взял  {bot_take} конфет и победил .\n'
                             'Если хочешь продолжить играть , отправь сообщение :  /start .\n'
                             'Если хочешь поменять условия игры ,отправь сообщение : /set и кол-во конфет через пробел')
        new_game = False
    else:
        remainder = total % (max_candy+1)
        bot_take = remainder if remainder != 0 else max_candy
        total -= bot_take
        await message.answer(f'Бот взял  {bot_take} конфет '
                             f' на столе осталось {total}')


def swith_player():
    global duel
    global current
    if current == duel[0]:
        current = duel[1]
    else:
        current = duel[0]


def enemy_id():
    global duel
    global current
    if current == duel[0]:
        return duel[1]
    else:
        return duel[0]
