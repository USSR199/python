from random import *
import os

def who_plays():
    player_1 = input('Ваше имя: ')
    player = input('С кем играете? игрок №2, бот, иибот: ')
    player_2 = ''
    if player == 'игрок №2':
        player_2 = input('Как его имя: ')
    elif player == 'бот':
        player_2 = 'бот'
    else:
        if player == 'иибот':
            player_2 = 'иибот'
    return player_1, player_2

def lot(play_1, play_2):
    lots = randint(1, 2)
    if lots == 1:
        first = play_1
        second = play_2
    else:
        first = play_2
        second = play_1
    print(f'Первый ходит {first}, а второй {second}')
    return(first, second)

def start_game(play1, play2):
    if play1 == 'иибот' or play2 == 'иибот':
        return game_iibot(play1, play2)
    else:
        return game(play1, play2)

def game(play_1, play_2):
    count_candies = 2021
    max_move = 28
    count = 0
    while count_candies > 0:
        if count == 0:
            if play_1 == 'бот':
                if count_candies > 28 and count_candies <= 2021:
                    move = randint(1, 28)
                    print(f'ходит {play_1}: {move} конфет')
                else:
                    move = count_candies
                count_candies -= move
            else:
                move = int(input (f'Твой ход {play_1}: ' ))
                if move > max_move or move < 0:
                    move = int(input('Уверен? Попробуй ещё раз: '))
                count_candies -= move
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
            count = 1
        else:
            print(f'Ты выиграл {play_1}!')
        if count == 1:
            if play_2 == 'бот':
                if count_candies > 28 and count_candies <= 2021:
                    move = randint(1, 28)
                    print(f'ходит {play_2}: {move} конфет')
                else:
                    move = count_candies
                count_candies -= move
            else:
                move = int(input (f'Теперь твой ход {play_2} : ' ))
                if move > max_move or move < 0:
                    move = int(input('Уверен? Попробуй ещё раз: '))
                count_candies -= move
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
            count = 0
        else:
            print(f'Ты выиграл {play_2}!')

def game_iibot(play_1, play_2):
    count_candies = 2021
    max_move = 28
    count = 0
    while count_candies > 0:
        if count == 0:
            if play_1 == 'иибот':
                if count_candies == 2021:
                    move_bot = 20
                    print(f'ходит {play_1}: {move_bot} конфет')
                elif count_candies > 28 and count_candies <= 2001:
                    move_bot = 29 - move_play_2
                    print(f'ходит {play_1}: {move_bot} конфет')
                else:
                    move_bot = count_candies
                count_candies -= move_bot
            else:
                move = int(input (f'Твой ход {play_1}: ' ))
                if move > max_move or move < 0:
                    move = int(input('Уверен? Попробуй ещё раз: '))
                count_candies -= move
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
            count = 1
        else:
            print(f'Выиграл {play_1}!')
        if count == 1:
            if play_2 == 'иибот':
                if count_candies != 2001:
                    if count_candies > 28 and count_candies <= 2021:
                        move_bot = 29 - move
                        print(f'ходит {play_2}: {move_bot} конфет')
                    else:
                        move_bot = count_candies
                    count_candies -= move_bot
                else:
                    print('Я не хочу играть')
                    break
            else:
                move_play_2 = int(input (f'Теперь твой ход {play_2} : ' ))
                if move_play_2 > max_move or move_play_2 < 0:
                    move_play_2 = int(input('Уверен? Попробуй ещё раз: '))
                count_candies -= move_play_2
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
            count = 0
        else:
            print(f'Выиграл {play_2}!')

players = who_plays()
lots = lot(players[0], players[1])
start_game(lots[0], lots[1])
