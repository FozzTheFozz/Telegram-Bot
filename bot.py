from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackContext
from telegram import *
from html import escape
import pickledb
"""
This is a shitty Python telegram bot!
The available commands are:
/start
/ban
help
/rules
"""
updater = Updater(token='Enter your token here', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hello, {user.mention_markdown_v2()}\! How can i help you?',
        reply_markup=ForceReply(selective=True),
    )
def rules(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="<ADD YOUR BOT RULES HERE!>")

def ban(update, context):
  context.bot.ban_chat_member(chat_id=update.effective_chat.id, user_id="Add User id")

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f"{member.full_name} has joined the group.")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id,text='<b>Have a look at here</b> <a href="http://google.com">Here!</a>', parse_mode=ParseMode.HTML)


help = CommandHandler('help', help_command)
dispatcher.add_handler(help)
add_group = MessageHandler(Filters.status_update.new_chat_members, add_group)
dispatcher.add_handler(add_group) 
ban = CommandHandler('ban', ban)
dispatcher.add_handler(ban)
rules = CommandHandler('rules', rules)
dispatcher.add_handler(rules)
start = CommandHandler('start', start)
dispatcher.add_handler(start)
# To start the bot run:
updater.start_polling()
