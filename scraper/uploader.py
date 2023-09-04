#!/usr/bin/env python3

'''Module to convert csv data aboout GPU content into python object'''

import csv
import logging
import re
from typing import List

#import pandas

#from models import Card

log = logging.getLogger('dexia')


# def upload(source: str) -> List[Card]:
#     '''Upload local file to create data for api'''
#     log.info(f'Uploading file {source}...')

#     cards: List[Card] = []

#     with open(source, 'r', encoding='utf-8') as document:
#         df = pandas.read_csv(document, header=2)
#         for _, row in df.iterrows():
#             cards.append(Card.load(row))
#     log.info(f'File {source} uploaded')
#     log.info(f'Loaded {len(cards)} GPU')
#     return cards


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
