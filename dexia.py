import logging
import os
import sys
from multiprocessing import Process

import api
import config.constant as CONSTANTS
import helper
import scraper

from config import Config, load

log = logging.getLogger("dexia")


def main():
    '''
    entrypoint
    '''
    setup_logger()
    config: Config = load('config.json')
    set_log_level(config)
    log.debug("Project : %s - Version : %s", CONSTANTS.project, CONSTANTS.version)

    # TODO gerer la partie scrap et la partie api 
    # TODO finir le docker file

     # Process Download GSheet file only if config accept to download
    log.info('Web Scraper: %s', 'active' if config.scraper else 'disable')

    if config.scraper:
        Process(target=scraper.start,
                args=(config.url,))\
            .start()
        
    # Launch API
    Process(target=api.start,
            args=(config,))\
        .start()


def setup_logger():
    '''Setup logging format'''
    log_formatter = '[%(asctime)s] | %(levelname)s : %(message)s'
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    formatter = logging.Formatter(log_formatter, date_format)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)

    log_file: str = f"Logs/{helper.get_date()}.log"
    create_logs_folder(log_file)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(stdout_handler)


def set_log_level(config: Config):
    '''Set level log'''
    level: int = logging.DEBUG if config.debug else logging.INFO
    log.setLevel(level)
    log.debug('Set debug mode')


def create_logs_folder(filepath: str) -> None:
    '''Create logs folder if not exists'''
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.mkdir(dirname)


if __name__ == '__main__':
    main()
