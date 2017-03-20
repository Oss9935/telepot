import sys
import time
import telepot
import configparser

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	# echo text type message
	if content_type == 'text':
		bot.sendMessage(chat_id, msg['text'])

# read bot's token from configfile
def getBotToken(configFilePath):
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	return TOKEN

if __name__ == "__main__":

	configFilePath = 'bbkimBot_config.conf'
	TOKEN = getBotToken(configFilePath)

	bot = telepot.Bot(TOKEN)
	bot.message_loop(handle)
	print('Listening...')

	# keep the program running
	while 1:
		time.sleep(10)