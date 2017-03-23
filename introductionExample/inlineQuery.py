import sys
import telepot
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
import configparser

# read bot's token from configfile
def getBotToken(configFilePath):
	config = configparser.ConfigParser()
	config.read(configFilePath)
	TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

	return TOKEN

def on_inline_query(msg):
	# telepot.glance() works on any type of messages. Just give it the flavor.
	# In this case, flavor should be 'inline_query'
    query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
    print ('Inline Query:', query_id, from_id, query_string)

	# To construct an answer to inline query, 
	# use InlineQueryResultArticle, InputTextMessageContent namedtuple
    articles = [InlineQueryResultArticle(
                    id='abc',
                    title='ABC',
                    input_message_content=InputTextMessageContent(
                        message_text='Hello'
                    )
               )]

    bot.answerInlineQuery(query_id, articles)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)


if __name__ == "__main__":

	# read bot's token from configfile
	configFilePath = 'bbkimBot_config.conf'
	TOKEN = getBotToken(configFilePath)

	bot = telepot.Bot(TOKEN)
	bot.message_loop({'inline_query' : on_inline_query,
		'chosen_inline_result' : on_chosen_inline_result},
		run_forever = 'Listening...')
