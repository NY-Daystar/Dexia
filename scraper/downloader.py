#!/usr/bin/env python3

'''Module to Scrap data about Formula 1'''
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

import schedule

from config import Config
from helper import get_mp_logger, is_new_file, path_combine
from models import Calendar
from scraper import constants

from .entity import CalendarEntity

log = get_mp_logger()

def start(config: Config):
    '''Launch downloader to scrap data'''

    log.info('Cron downloader setup at every minutes')

    # Scrap web data one time to get it instantly
    scrap(config)

    log.info('Cron downloader setup at every hour')
    schedule.every(1).hours.at(':00').do(scrap, config)

    while 1:
        try:
            schedule.run_pending()
        except KeyboardInterrupt:
            sys.exit(0)



def scrap(config: Config) -> Calendar:
    '''
    Download source GSheet file in csv into destination file
    tab parameter indicate which tab you want to download first is 0
    '''
    calendar: Calendar = CalendarEntity().scrap(config.url)

    if calendar is None:
        log.warning('No calendar was found\nSkip the end process')
        return

    year: int = CalendarEntity().scrap_year(config.url)
    log.info("Year scrapped : %s", year)
    calendar.set_year(year)
    calendar.set_version(constants.DOCUMENT_VERSION)

    # Display in log
    log.info(calendar)
    [log.debug(gp) for gp in calendar.grand_prix]

    file: Path = path_combine(config.folder, constants.FILE)
    is_saved: bool = save_data(calendar, config.folder, file)

    log.info("data %s into file: %s", 'saved' if is_saved is True else 'not saved', file) 

def save_data(calendar:Calendar, folder: Path, file: Path) -> bool:
    """'Copy calendar content into files

    Args:
        calendar (Calendar): calendar to saved in json file
        folder (Path): folder to save json backup files
        file (Path): file to save data

    Returns:
        bool: True if saved, otherwise False
    """ 
    if calendar is None:
        log.warning('Calendar cannot be saved is None')
        return False

    if not os.path.exists(folder):
        os.mkdir(folder)

    # Write in backup file 
    dtime: str = datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    backup_file: Path = path_combine(folder, f'data_{dtime}.json')
    log.debug('Creating backup file: %s', backup_file)
    with open( backup_file , "w", encoding='utf-8' ) as file_descriptor:
        json.dump(calendar.to_dict(), file_descriptor, ensure_ascii=False, indent=4)

    # Write file if not exist or new changes
    if not file.exists():
        log.debug('file %s doesn\'t exist copying backup file %s', file, backup_file)
        shutil.copy(backup_file, file)

    # Detect changes
    if is_new_file(file, backup_file):
        log.info("New content in backup file (%s), copying into (%s)", backup_file, file )
        shutil.copy(backup_file, file)
    else:
        log.warning("Content not changed, No copy of backup file (%s) into file (%s)", backup_file, file)

    return True
