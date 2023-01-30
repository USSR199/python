count_of_candies = 2021
total = count_of_candies
new_game = False
bot_level = 1


def set_count_of_candies(value: int):
    global count_of_candies
    count_of_candies = value


def get_total():
    global total
    return total


def take_candies(taken_candies: int):
    global total
    total -= taken_candies


def start_new_game():
    global new_game
    global total
    global count_of_candies
    if new_game:
        new_game = False
    else:
        new_game = True
        total = count_of_candies


def game():
    global new_game
    return new_game


def get_bot_level():
    global bot_level
    return bot_level


def change_bot_level():
    global bot_level
    if bot_level == 1:
        bot_level = 0
    else:
        bot_level = 1
