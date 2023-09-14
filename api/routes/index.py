'''All API route'''
from fastapi import FastAPI

#from api.routes import admin, card, cards
from api.routes import admin
from config import Config
from helper import get_mp_logger

log = get_mp_logger()


def setup(app: FastAPI, config: Config):
    '''Setup routes for FastAPI'''

    #csv_file: str = config.file.destination

    admin.setup(app)
    #cards.setup(app, csv_file)
    #card.setup(app, csv_file)
