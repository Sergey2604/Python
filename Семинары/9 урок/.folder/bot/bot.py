from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater("5578511222:AAEiPh5Pf33Is8m2Vu-mabIjQs8ZYHyh8yQ")

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))

print('server start')
updater.start_polling()
updater.idle()
