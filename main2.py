from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_API_TOKEN' with your actual bot API token
API_TOKEN = 'YOUR_API_TOKEN'

# Dictionary to store personal data
personal_data = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me your personal data.')

def store_data(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    personal_data[user_id] = text
    update.message.reply_text('Your data has been stored.')

def main() -> None:
    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, store_data))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()