#!/usr/bin/env python3

'''Module to convert csv data about Calendar and F1 Grand Prix in python object'''

import csv
import re
import sys

import pandas
import schedule

from config import Config
from helper import get_mp_logger
from models import Calendar

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


def get_version(source: str) -> str:
    '''Get Version of local file'''
    log.info(f'Uploading file {source}...')

    version: str = "0"
    with open(source, 'r', encoding='utf-8') as document:
        rows = list(csv.reader(document))
        version_str: str = rows[1][0]
        try:
            version = re.search(r"^Version:? (.*)$", version_str).group(1)
        except AttributeError:
            pass

    log.info(f'File {source} uploaded')
    log.info(f'Loaded document version : {version}')
    return version
