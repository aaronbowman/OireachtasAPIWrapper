# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging

import Wrapper


def print_content():
    reply = Wrapper.Response().make_request(endpoint='https://api.oireachtas.ie/v1/debates')
    print(reply.content)




# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    logging.info('Started')
    print_content()
    logging.info('Finished')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
