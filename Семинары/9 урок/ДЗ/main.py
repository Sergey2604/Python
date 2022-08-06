from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

import commands as c

updater = Updater("5144126383:AAFE7pLwJnk-EuC0taT6fpQ-6oVzJ7tJk9U")


updater.dispatcher.add_handler(CommandHandler('start', c.start))
