import sys
import telepot
from telepot.delegate import pave_event_space, per_inline_from_id, create_open
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
import configparser

# read bot's token from configfile
def getBotToken(configFilePath):
    config = configparser.ConfigParser()
    config.read(configFilePath)
    TOKEN = config.get('bbkim_test_bot_INFO', 'TOKEN')

    return TOKEN

class QueryCounter(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    def __init__(self, *args, **kwargs):
        super(QueryCounter, self).__init__(*args, **kwargs)
        self._count = 0

    def on_inline_query(self, msg):
        def compute():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)

            self._count += 1
            text = '%d. %s' % (self._count, query_string)

            articles = [InlineQueryResultArticle(
                            id='abc',
                            title=text,
                            input_message_content=InputTextMessageContent(
                                message_text=text
                            )
                       )]

            return articles

        self.answerer.answer(msg, compute)

    def on_chosen_inline_result(self, msg):
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)

if __name__ == "__main__":

    # read bot's token from configfile
    configFilePath = 'bbkimBot_config.conf'
    TOKEN = getBotToken(configFilePath)

    bot = telepot.DelegatorBot(TOKEN, [
        pave_event_space()(
            per_inline_from_id(), create_open, QueryCounter, timeout=10),
    ])
    bot.message_loop(run_forever='Listening ...')