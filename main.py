from telegram import Update

from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Telegram bot token

TOKEN = '6242918828:AAHH0M0GZC4rjF57bZIvbFMMaOCSSs0ZsHw'

# Source and destination chat IDs

SOURCE_CHAT_ID = -1001932388552  # Replace with the source channel or group ID

DESTINATION_CHAT_ID = -1001914288789  # Replace with the destination channel or group ID

def forward_messages(update: Update, context: CallbackContext):

    message = update.message

    if message.chat_id == SOURCE_CHAT_ID:

        context.bot.forward_message(chat_id=DESTINATION_CHAT_ID, from_chat_id=message.chat_id, message_id=message.message_id)

def main():

    # Create the updater and dispatcher

    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    

    # Register the message handler

    dispatcher.add_handler(MessageHandler(Filters.chat(chat_id=SOURCE_CHAT_ID), forward_messages))

    

    # Start the bot

    updater.start_polling()

    updater.idle()

if name == 'main':

    main()
