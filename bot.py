import logging
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackContext, Updater
import telegram.ext as telegramext 
from html import escape
from telegram import Update
"""
This is a shitty Python telegram bot!
The available commands are:
/start
/ban
/kitty
/help
/rules
"""
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(
    format='%(asctime)s – %(levelname)s – %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)


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

def send_cat(update: Update, context: CallbackContext) -> None:
    update.message.reply_photo("http://placekitten.com/720/450")


kitty = CommandHandler('kitty',send_cat)
dispatcher.add_handler(kitty)
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
logging.info('Bot has started')
