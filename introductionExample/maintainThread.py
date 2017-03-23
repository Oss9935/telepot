# This bot simply echo inline query message

import sys
import telepot
from telepot.delegate import pave_event_space, per_chat_id, create_open
import configparser

# read bot's token from configfile
def getBotToken(configFilePath):
    config = configparser.ConfigParser()
    config.read(configFilePath)
    TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

    return TOKEN


class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)
        self._count = 0

    def on_chat_message(self, msg):
        self._count += 1
        self.sender.sendMessage(self._count)


if __name__ == "__main__":

    # read bot's token from configfile
    configFilePath = 'bbkimBot_config.conf'
    TOKEN = getBotToken(configFilePath)


    bot = telepot.DelegatorBot(TOKEN, [
        pave_event_space()(
            per_chat_id(), create_open, MessageCounter, timeout=10),
    ])
    bot.message_loop(run_forever='Listening ...')