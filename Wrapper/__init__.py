import logging

from .api import API as Response

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='OireachtasWrapper_API.log', level=logging.DEBUG, format=formatter)