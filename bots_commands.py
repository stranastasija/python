from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name} !')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi - приветствие\n/time - время\n/sum - сумма двух чисел, введенных через пробел\n/dif - разность двух чисел, введенных через пробел\n/motive - небольшая мотивация для тебя\n/love - признание для тебя\n/bye - попрощаемся?\n/help - список всех команд')

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print (msg)
    items = msg.split()
    x = int (items[1])
    y = int (items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

def dif_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print (msg)
    items = msg.split()
    x = float (items[1])
    y = float (items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')

def motive_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{update.effective_user.first_name}, в этой жизни бывает много плохого, но хорошего в разы больше ;) Никогда не грусти и не сворачивай со своего пути!')

def love_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{update.effective_user.first_name}, I love you so much!!!')

def bye_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Пока, {update.effective_user.first_name}! Возвращайся ко мне еще! ;)')
