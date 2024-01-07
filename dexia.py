"""Main module"""
from multiprocessing import Process

import api
import scraper
from config import Config
from helper import get_mp_logger

log = get_mp_logger()

__project__: str = 'Dexia'
__version__: str = 'v1.0.0'


def main():
    """
    Entrypoint of the program 
    - Load configuration file (config.json)
    - Setup Logger
    - Launch multiprocessing (scraper + api)
    """
    log.debug("Project : %s - Version : %s", __project__, __version__)

    config: Config = Config.load('config.json')

    # Process Web scraping, only if config accept to scrap
    log.info('Web Scraper: %s', 'active' if config.scraper else 'disable')

    # Launch Scraper if activated
    if config.scraper:
        Process(target=scraper.start, args=(config,)).start()

    # Launch API
    Process(target=api.start, args=(config, )).start()


if __name__ == '__main__':
    main()
