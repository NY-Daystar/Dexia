#!/usr/bin/env python3

'''Module to fetch Google Sheet about GPU content'''
import hashlib
import logging
import shutil
import sys
from pathlib import Path
from typing import Tuple
from datetime import datetime

import requests
import schedule

from config import FileConfig, constants

log = logging.getLogger('dexia')

### TODO faire le scrapper

def start(config: FileConfig):
    '''Launch run downloader to get GSheet GPU data'''

    src_file: str = config.source
    dest_file: Path = Path(config.destination)

    # Download the GSheet one time to get it instantly
    update(src_file, dest_file)

    log.info('Cron downloader setup at every minutes')
    schedule.every(1).minutes.at(':00').do(update, src_file, dest_file)

    while 1:
        try:
            schedule.run_pending()
        except KeyboardInterrupt:
            sys.exit(0)


def update(file_id: str, destination: Path = '.', tab: int = 0):
    '''
    Download source GSheet file in csv into destination file
    tab parameter indicate which tab you want to download first is 0
    '''

    # Setup folder content/ if not created
    Path(destination.parent).mkdir(parents=True, exist_ok=True)

    content, err = download(file_id, tab)
    if err is not None:
        log.error(f'Can\'t update the csv file {err}')
        return

    log.debug("Comparing current file with content downloaded")
    if not is_new_file(destination, content):
        log.info("No new content found from GSheet, skip.")
        return
    log.info("New content found from GSheet")

    log.info("Save into backup file old content")
    file_backup: str = save_file(destination)
    log.info(f"Backup saved: {file_backup}")

    # Write CSV
    log.info(f'Writing content into {destination}')
    with open(destination, 'w', encoding="utf-8") as document:
        document.write(content)
    log.info(f'File {destination} written')


def download(file_id: str, tab: int = 0) -> Tuple[bool, Exception]:
    '''Download source GSheet file on tab and return its content'''
    source: str = f'https://docs.google.com/spreadsheets/d/e/{file_id}'\
        f'/pub?gid={tab}&single=true&output=csv'
    log.debug(f'Downloading file: {source}')

    # Download from google
    response = requests.get(source)

    if response.status_code != 200 or response.content == b'':
        log.error(
            f'Can\'t download GSheet file status: {response.status_code}, '
            'reason: {response.reason}'
        )
        return None, Exception(f"Error code: {response.status_code}, reason: {response.reason}")

    content: str = response.content.decode("utf-8")
    log.debug(f'File {source} downloaded')
    return content, None


def is_new_file(current_file: Path, new_file_content: str) -> bool:
    '''Compare MD5 checksum of current file and new content downloaded from Google'''
    return file_checksum(current_file, "file") != file_checksum(new_file_content, "str")


def file_checksum(source: str, content_type: str = "file") -> str:
    '''Return md5 checksum of a file or a string'''
    md5_hash = hashlib.md5()

    if content_type == "str":
        return hashlib.md5(source.encode('utf-8')).hexdigest()
    elif content_type == "file":
        try:
            with open(source, "rb") as document:
                content: bytes = document.read()
                md5_hash.update(content)

                digest: str = md5_hash.hexdigest()
                return digest
        except FileNotFoundError:
            return "0"
    else:
        return None


def save_file(file: Path) -> str:
    '''Copy old file on another filename'''
    if not file.exists():
        return
    dtime: datetime = datetime.now()
    time_formatted: str = dtime.strftime('%Y-%m-%d_%H:%M:%S')
    filename: str = f"gpus_{time_formatted}.csv"
    backup_file: Path = Path(f'{constants.DEST_FOLDER}/{filename}')
    shutil.copy(file, backup_file)
    return filename
