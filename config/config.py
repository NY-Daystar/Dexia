'''Config of Dexia'''
import logging

from .constant import DEFAULT_DEBUG

'''Configuration class'''


log = logging.getLogger('dexia')


class Config:
    '''Config of the application'''
    debug: str = DEFAULT_DEBUG
