from logging import DEBUG, FileHandler, Formatter, Logger, StreamHandler
from multiprocessing import get_logger
from os import mkdir
from os.path import dirname, exists
from pathlib import Path

from .date import get_date

PATH=f"Logs/logs-{get_date()}.log"

# TODO gerer proprement la variable path via la config
# TODO gerer proprement la variable level en la chargeant depuis la config

def get_mp_logger(file_path: Path = Path(PATH), level: int = DEBUG )-> Logger:
    """Handle multiprocessing logs

    Args:
        file_path (Path, optional): file to save logs. Defaults to Path(f"Logs/logs-{get_date()}.log").
        level (int, optional): level to display. Defaults to DEBUG.

    Returns:
        Logger: logger to write logs
    """    
    logger = get_logger()
    logger.setLevel(level)
    formatter = Formatter('%(asctime)-2s - %(levelname)-8s - [%(filename)s:l-%(lineno)d] - %(message)s')

    # Handle logs folder
    create_logs_folder(file_path)

    # File logger
    file_handler = FileHandler(file_path, encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Console logger
    stdout_handler = StreamHandler()
    stdout_handler.setFormatter(formatter)

    if not logger.handlers: 
        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
 
    return logger


def create_logs_folder(file_path: str) -> None:
    """Create logs folder if not exists

    Args:
        filepath (str): filepath of log where create dir
    """    
    folder = dirname(file_path)
    if not exists(folder):
        mkdir(folder)
