#!/usr/bin/env python3

'''Module to convert csv data about Calendar and F1 Grand Prix in python object'''

import json
import sys

import pandas
import schedule

from config import Config
from helper import get_mp_logger, path_combine
from models import Calendar
from scraper import constants

log = get_mp_logger()

def start(config: Config) -> Calendar:
    upload(config)

    log.info('Cron uploader setup at every hours')
    schedule.every(1).hours.at(':00').do(upload, config.url)

    while 1:
        try:
            schedule.run_pending()
        except KeyboardInterrupt:
            sys.exit(0)

## TODO a faire et a commenter
def upload(Config: str) -> Calendar:
    '''Upload local file to create data for api'''
    log.info(f'Uploading file {source}...')

    calendar: Calendar = Calendar()

    with open(source, 'r', encoding='utf-8') as document:
        df = pandas.read_csv(document, header=2)
        for _, row in df.iterrows():
            print(row)
            #calendar.append(GrandPrix.load(row))
    log.info(f'File {source} uploaded')
    log.info(f'Loaded {len(calendar.grand_prix)} GPU')
    return calendar.grand_prix

def get_last_document(config: Config) -> str:
    '''
    Get path of last .json document uploaded
    '''
    return path_combine(config.folder, constants.FILE)

def get_version(source: str) -> int:
    '''Get version of local file'''
    log.info(f'Loading document {source}...')

    default_version: int = 1
    with open(source, 'r', encoding='utf-8') as document:
        data = json.load(document)
        try:
            version = data.get('version', default_version)
        except AttributeError:
            pass

    log.info(f'Loaded document version : {version}')
    return version
