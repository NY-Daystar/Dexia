import logging
import os
import sys

import config.constant as CONSTANTS
import helper
import scraper
from models import Calendar, GrandPrix

log = logging.getLogger("dexia")


def main():
    '''
    entrypoint
    '''
    setup_logger()
    set_log_level()
    log.debug("Project : %s - Version : %s", CONSTANTS.project, CONSTANTS.version)

    # Get calendar
    calendar: Calendar = scraper.scrap_calendar(
        url="https://f1i.autojournal.fr/calendrier-f1-2023-dates-horaires-grands-prix")

    # TODO pour chacun des grand prix recuperer le detail
    # FP1, FP2, FP3, QUALIF et COURSE

    # For each grand prix get all data
    for gp in calendar.grand_prix:
        print(gp)


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


def set_log_level():
    '''Set level log'''
    level: int = logging.DEBUG if helper.is_arg_debug() else logging.INFO
    log.setLevel(level)
    log.debug('Set debug mode')


def create_logs_folder(filepath: str) -> None:
    '''Create logs folder if not exists'''
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.mkdir(dirname)


if __name__ == '__main__':
    main()
