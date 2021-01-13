from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram_utils
import config
import api_utils

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    updater = Updater(config.bot_token, use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", telegram_utils.start))
    dispatcher.add_handler(CommandHandler("help", telegram_utils.help))
    dispatcher.add_handler(CommandHandler("latest", telegram_utils.latest))
    dispatcher.add_handler(CommandHandler("recent", telegram_utils.recent))
    dispatcher.add_handler(CommandHandler("notice", telegram_utils.notice))
    dispatcher.add_handler(CommandHandler("today", telegram_utils.today))
    #dispatcher.add_handler(CommandHandler("subscribe", telegram_utils.subscribe))
    dispatcher.add_handler(MessageHandler(Filters.text, telegram_utils.response_to_message))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()