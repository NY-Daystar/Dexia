'''All API route'''
import logging

from fastapi import FastAPI

#from api.routes import admin, card, cards
from api.routes import admin
from config import Config
log = logging.getLogger('dexia')


def setup(app: FastAPI, config: Config):
    '''Setup routes for FastAPI'''

    #csv_file: str = config.file.destination

    admin.setup(app)
    #cards.setup(app, csv_file)
    #card.setup(app, csv_file)
