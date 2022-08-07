from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import token_bot as token
import commands as c

updater = token.token_bot


updater.dispatcher.add_handler(CommandHandler('start', c.start))
