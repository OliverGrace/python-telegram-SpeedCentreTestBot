# The MIT License (MIT)
# Copyright © 2021 OliverGrace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import logging
import threading
import telegram
from clash_sub_converter import*
from add import add_node, random
from get_link import*
from listname import*
from telegram import Update, bot, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

my_user_id = '你的用户ID'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

access_list = ''


def update_access_list():
    access_file = open('access.txt', 'r')
    global access_list
    access_list = access_file.read()
    access_file.close()


update_access_list()


def timer(bbot, chatid, sent_message):
    bbot.deleteMessage(chat_id=chatid, message_id=sent_message)



def start(update: Update, _: CallbackContext):
    if check_access(update):
        response_message = 'START MESSAGE'
    else:
        response_message = 'REJECT MESSAGE'
    # timer(bbot, update.message.chat_id, sent_message.message_id)
    bbot = Bot(token='BOT_TOKEN')
    sent_message = update.message.reply_text(response_message)
    arg = [bbot, update.message.chat_id, sent_message.message_id]
    timerx = threading.Timer(10, function=timer, args=arg)
    timerx.start()


    # print(str(to_check_id))
    # if str(to_check_id) in access_list:
    #     response_message = 'START MESSAGE'
    # else:
    #     response_message = 'REJECTED MESSAGE'


    # bbot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)

def check_access(update: Update) -> bool:
    to_check_id = update.message.from_user.id
    print(str(to_check_id))
    if str(to_check_id) in access_list:
        return True
    else:
        return False


def add_access(update: Update, context: CallbackContext):
    to_check_id = str(update.message.from_user.id)
    if to_check_id == 'START MESSAGE' or to_check_id == '1341501740':
        access_id = context.args
        access_file = open('access.txt', 'a+')
        access_file.writelines('$' + ''.join(access_id))
        access_file.close()
        update_access_list()
        sent_message = update.message.reply_text('已经添加'+str(access_id)+'的访问权限')

        bbot = Bot(token='BOT_TOKEN')
        arg = [bbot, update.message.chat_id, sent_message.message_id]
        timerx = threading.Timer(10, function=timer, args=arg)
        timerx.start()
    else:
        sent_message = update.message.reply_text('REJECTED MESSAGE')

        bbot = Bot(token='BOT_TOKEN')
        arg = [bbot, update.message.chat_id, sent_message.message_id]
        timerx = threading.Timer(10, function=timer, args=arg)
        timerx.start()


def subcon(update: Update, context: CallbackContext):
    if check_access(update):
        link = ''.join(context.args)
        response_message = '转换clash订阅完成！订阅如下：'+'\n'+sub_convert(link)
    else:
        response_message = 'REJECTED MESSAGE'
    # timer(bbot, update.message.chat_id, sent_message.message_id)
    bbot = Bot(token='BOT_TOKEN')
    sent_message = update.message.reply_text(response_message)
    arg = [bbot, update.message.chat_id, sent_message.message_id]
    timerx = threading.Timer(10, function=timer, args=arg)
    timerx.start()


def add_(update: Update, context: CallbackContext):
    if check_access(update):
        sent_message = update.message.reply_text(add_node(context.args[0], context.args[1])+'\n')
    else:
        sent_message = update.message.reply_text('REJECTED MESSAGE')
    # timer(bbot, update.message.chat_id, sent_message.message_id)
    bbot = Bot(token='BOT_TOKEN')
    arg = [bbot, update.message.chat_id, sent_message.message_id]
    timerx = threading.Timer(10, function=timer, args=arg)
    timerx.start()

def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    sent_message = update.message.reply_text('Help!')
    bbot = Bot(token='BOT_TOKEN')
    arg = [bbot, update.message.chat_id, sent_message.message_id]
    timerx = threading.Timer(10, function=timer, args=arg)
    timerx.start()


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    sent_message = update.message.reply_text(update.message.text)
    bbot = Bot(token='BOT_TOKEN')
    arg = [bbot, update.message.chat_id, sent_message.message_id]
    timerx = threading.Timer(10, function=timer, args=arg)
    timerx.start()


def getlink(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    if check_access(update):
        if get_link(''.join(context.args), convert()) == 1:
            f = open("sub_found.txt", "r", encoding="GBK", errors="ignore")
            f.seek(0)
            sent_message = update.message.reply_text(f.read())
            f.close()

            bbot = Bot(token='BOT_TOKEN')
            arg = [bbot, update.message.chat_id, sent_message.message_id]
            timerx = threading.Timer(10, function=timer, args=arg)
            timerx.start()
        else:
            sent_message = update.message.reply_text('LINK NOT FOUND')
            bbot = Bot(token='BOT_TOKEN')
            arg = [bbot, update.message.chat_id, sent_message.message_id]
            timerx = threading.Timer(10, function=timer, args=arg)
            timerx.start()
    else:
        sent_message = update.message.reply_text('REJECTED MESSAGE')
        bbot = Bot(token='BOT_TOKEN')
        arg = [bbot, update.message.chat_id, sent_message.message_id]
        timerx = threading.Timer(10, function=timer, args=arg)
        timerx.start()



def list_name(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    if check_access(update):
        sent_message = update.message.reply_text(listname())
        bbot = Bot(token='BOT_TOKEN')
        arg = [bbot, update.message.chat_id, sent_message.message_id]
        timerx = threading.Timer(15, function=timer, args=arg)
        timerx.start()
    else:
        sent_message = update.message.reply_text('REJECTED MESSAGE')
        bbot = Bot(token='BOT_TOKEN')
        arg = [bbot, update.message.chat_id, sent_message.message_id]
        timerx = threading.Timer(10, function=timer, args=arg)
        timerx.start()


def random_node(update: Update, context: CallbackContext):
    if check_access(update):
        num = ''.join(context.args)
        sent_message = update.message.reply_text('\n'+str(random(num)))
    else:
        sent_message = update.message.reply_text('REJECTED MESSAGE')
    # timer(bbot, update.message.chat_id, sent_message.message_id)
    bbot = Bot(token='BOT_TOKEN')
    arg = [bbot, update.message.chat_id, sent_message.message_id]
    timerx = threading.Timer(30, function=timer, args=arg)
    timerx.start()


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("BOT_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("getlink", getlink))
    dispatcher.add_handler(CommandHandler("listname", list_name))
    dispatcher.add_handler(CommandHandler("addaccess", add_access))
    dispatcher.add_handler(CommandHandler("add", add_))
    dispatcher.add_handler(CommandHandler("random", random_node))
    dispatcher.add_handler(CommandHandler("convert", subcon))
    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
