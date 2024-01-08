__all__ = ['start']

from config import Config
from helper import get_mp_logger

from . import downloader

log = get_mp_logger()


def start(config: Config):
    """Launch scrap to download data

    Args:
        config (Config): config to scrap with urls, files to saved, and so on
    """
    log.debug('Scrap - start downloader')
    downloader.start(config)
