import random

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f' Вы хотите сыграть в крестики-нолики?, {update.effective_user.first_name}')
    if update.message.text == ("да" or "Да"):
        game()
    else:
        update.message.reply_text('До свидания!')


def game():
    print(pole())
    first_turn()
    turns()


def pole():
    pole='  |   |   |   \n' \
         '  |   |   |   \n' \
         '  |   |   |   '
    return pole

def first_turn():
    global bot, gamer
    bot = 1
    gamer = 2
    count = random.Random(2)
    if count == 1:
        return bot
    elif count == 2:
        Update.message.text('Чтобы выбрать клетку, отправьте в сообщении от 1 до 9, '
                            'где 1-3 - это верхний ряд слева-направо, 4-6 - средний ряд, 7-9 - нижний ряд')


def turns():
    bot_turn = 0
    if first_turn == 1:
        bot_turn = random.Random(10)
    a = Filters.text

