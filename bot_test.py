from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bots_commands import *

updater = Updater('5243461107:AAFLu5Yt5bg1pZVTQ811K1ockmkuKIPInXU')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print ('server start')

updater.start_polling()
updater.idle()