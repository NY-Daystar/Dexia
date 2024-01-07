#!/usr/bin/env python3

'''Module to convert csv data about Calendar and F1 Grand Prix in python object'''

import json

from config import Config
from helper import get_mp_logger, path_combine
from models import Calendar, GrandPrix
from scraper import constants

log = get_mp_logger()

def get_last_document(config: Config) -> str:
    '''
    Get path of last .json document uploaded
    '''
    source: str = path_combine(config.folder, constants.FILE)
    log.debug(f'Loading document {source}...')
    return source

def upload(config: Config) -> Calendar:
    '''Upload Calendar from local file to create data for api'''
    calendar: Calendar = Calendar()
    
    source = get_last_document(config)

    with open(source, 'r', encoding='utf-8') as document:
        data = json.load(document)
        try:
            calendar.set_version(data['version'])
            calendar.set_year(data['year'])
            for gp in data['grand_prix']:
                grandPrix : GrandPrix = GrandPrix(gp['index'], gp['name'], gp['date'])
                calendar.add_grand_prix(grandPrix)
        except Exception as e:
            log.error(e)
            return None

    log.info(f'Loaded document into calendar')
    return calendar

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
