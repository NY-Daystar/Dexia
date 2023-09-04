'''Config of Dexia'''
import json
import logging

import config.constant as CONSTANTS
from config.api import ApiConfig

'''Configuration class'''


log = logging.getLogger('dexia')


class Config:
    '''Config of the application'''
    debug: str = CONSTANTS.debug
    scraper: bool = True
    api: ApiConfig
    
#@classmethod
def load(cls, filepath: str) -> Config:
    '''Create config object loading data from config.json file'''
    config: Config = Config()
    with open(filepath, mode='r', encoding='utf-8') as document:
        json_data = json.load(document)
        config.debug = json_data.get('debug', False)
        config.downloader = json_data.get('downloader', True)
        config.api = ApiConfig().load(json_data.get('api', dict()))
    return config
