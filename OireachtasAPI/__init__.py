import logging

from .api import API as API
from .wrapper import Wrapper as Wrapper

logging.getLogger('OireachtasAPI').addHandler(logging.NullHandler())