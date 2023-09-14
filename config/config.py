'''Config of Dexia'''
import json

from config.api import ApiConfig


class Config:
    '''Config of the application'''
    debug: bool
    scraper: bool
    folder: str
    url: str
    api: ApiConfig

    @classmethod
    def load(cls, filepath: str) -> 'Config':
        """Create config object loading data from config.json file

        Args:
            filepath (str): file to read to create config

        Returns:
            Config: config based on content in `filepath`
        """        
        config: Config = Config()
        with open(filepath, mode='r', encoding='utf-8') as document:
            json_data = json.load(document)
            config.debug = json_data.get('debug', False)
            config.scraper = json_data.get('scraper', True)
            config.folder = json_data.get('folder', 'folder')
            config.url = json_data.get('url', None)
            config.api = ApiConfig().load(json_data.get('api', dict()))
        return config
    
    def __str__(self):
        return f'Config: debug: {self.debug} - scraper: {self.scraper} '\
            f'- folder: {self.folder} - url: {self.url} - Api: {self.api.host}:{self.api.port}'