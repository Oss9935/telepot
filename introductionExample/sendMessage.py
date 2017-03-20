import telepot
import configparser


# read bot's token from configfile
def getBotToken(configFilePath):
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	return TOKEN

if __name__ == "__main__":
	# read bot's token from configfile
	configFilePath = 'bbkimBot_config.conf'
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	bot = telepot.Bot(TOKEN)
	# You can get own real id in Receive Messages example's 'id' field.
	'''
	[{'message': {'chat': {'first_name': 'Nick',
                       'id': 999999999,		# <= This is your own id 
                       'type': 'private'},
              'date': 1465283242,
              'from': {'first_name': 'Nick', 'id': 999999999},
              'message_id': 10772,
              'text': 'Hello'},
  'update_id': 100000000}]
	'''	
	bot.sendMessage(181423919, 'Hey')