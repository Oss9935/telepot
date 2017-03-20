'''
Regardless of the type of objects received, 
telepot generically calls them “message” (with a lowercase “m”). 

A message’s flavor depends on the underlying object:
- a Message object gives the flavor chat
- a CallbackQuery object gives the flavor callback_query
- there are two more flavors, which you will come to shortly.
'''

import sys
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import configparser

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	# namedtuple to construct an InlineKeyboardMarkup
	# and an InlineKeyboardButton object
	keyboard = InlineKeyboardMarkup(inline_keyboard = [
			[InlineKeyboardButton(text = 'Press me', callback_data = 'Press')],
		])

	bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup = keyboard)

def on_callback_query(msg):
	# telepot.glance() works on any type of messages. Just give it the flavor.
	query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')

	print('Callback Query:', query_id, from_id, query_data)

	# Use Bot.answerCallbackQuery() to react to callback query
	bot.answerCallbackQuery(query_id, text = 'Got it')

# read bot's token from configfile
def getBotToken(configFilePath):
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	return TOKEN

if __name__ == "__main__":

	configFilePath = 'bbkimBot_config.conf'
	TOKEN = getBotToken(configFilePath)

	if len(sys.argv) == 2:
		TOKEN = sys.argv[1]

	bot = telepot.Bot(TOKEN)

	# To route messages according to flavor, give a routing table to Bot.message_loop()
	bot.message_loop({'chat' : on_chat_message,
					'callback_query' : on_callback_query})
	print('Listening...')

	while(1):
		time.sleep(10)
