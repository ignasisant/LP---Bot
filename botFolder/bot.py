from telegram.ext import Updater
from Handlers import Handlers
import logging
import pathlib
import os

token_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'token.txt')
TOKEN = open(token_path).read().strip()

def main():
    handlers = Handlers().getHandlers()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    for handler in handlers:
        dispatcher.add_handler(handler)
    updater.start_polling()

if __name__ == "__main__":
    main()

