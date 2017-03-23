# This bot simply echo inline query message

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
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)

        articles = [InlineQueryResultArticle(
                        id='abc',
                        title=query_string,
                        input_message_content=InputTextMessageContent(
                            message_text=query_string
                        )
                   )]

        return articles

    answerer.answer(msg, compute)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)


if __name__ == "__main__":

    # read bot's token from configfile
    configFilePath = 'bbkimBot_config.conf'
    TOKEN = getBotToken(configFilePath)


    bot = telepot.Bot(TOKEN)
    answerer = telepot.helper.Answerer(bot)

    bot.message_loop({'inline_query': on_inline_query,
                      'chosen_inline_result': on_chosen_inline_result},
                     run_forever='Listening ...')