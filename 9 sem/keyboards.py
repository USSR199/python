from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_step = ReplyKeyboardMarkup(resize_keyboard=True)
kb_end = ReplyKeyboardMarkup(resize_keyboard=True)

btn_new_game = KeyboardButton(text='/new_game')
btn_level = KeyboardButton(text='/level')
btn_stop = KeyboardButton(text='/stop_game')
btn_help = KeyboardButton(text='/help')

kb_start.add(btn_new_game, btn_level)

kb_step.row(btn_stop, btn_level)
kb_step.add(btn_help)

kb_end.row(btn_new_game, btn_level)
kb_end.add(btn_help)
