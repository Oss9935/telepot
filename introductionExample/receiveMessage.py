import telepot
import configparser
from pprint import pprint
import time

# read bot's token from configfile
def getBotToken(configFilePath):
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	return TOKEN

def handle(msg):
	pprint(msg)

if __name__ == "__main__":

	configFilePath = 'bbkimBot_config.conf'
	TOKEN = getBotToken(configFilePath)

	bot = telepot.Bot(TOKEN)
	# Before update, you have to send it a message first.
	print("Send a message to the bot using a telegram")
	time.sleep(3)	# wait for 3 Sec for the time you send the message.
	response = bot.getUpdates()
	pprint(response)

	# An easier way to receive messages
	print("An easier way to receive messages")
	print("Start : message Loop")
	bot.message_loop(handle)
	time.sleep(3)	# wait for 3 Sec for the time you send the message.