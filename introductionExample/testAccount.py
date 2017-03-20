import telepot
import configparser

if __name__ == "__main__":
	# read bot's token from configfile
	configFilePath = 'bbkimBot_config.conf'
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	# test the account
	bot = telepot.Bot(TOKEN)
	print(bot.getMe())