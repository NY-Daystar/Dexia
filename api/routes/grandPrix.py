'''GrandPrix routes'''
from typing import List

from fastapi import FastAPI, HTTPException

from config import Config
from helper import get_mp_logger
from models import Calendar
from scraper.uploader import upload

log = get_mp_logger()

def setup(app: FastAPI, config: Config):

    
    @app.get('/api/v1/calendar',
             tags=['Calendar'],
             summary='Get calendar of Formula 1  GPU data',
             description='Get all information about Formula 1 GrandPrix of the year',
             )
    def _():
        '''
        Define all grand prix in array
        '''
        calendar: Calendar = upload(config)
        return calendar

    @app.get('/api/v1/grandprix/{id}',
             tags=['GrandPrix'],
             summary='Get GrandPrix informations',
             description='Get details on specific GrandPrix',
             )
    def _(id: int):
        '''
        Get info about one specific grand prix
         Args:
        id (int): index of grand prix that we are looking for
        '''
        calendar: Calendar = upload(config)
        grandPrix: str = calendar.get_grand_prix(id)

        if(grandPrix is None):
            raise HTTPException(
                status_code=404, 
                detail={
                    'status': 'KO',
                    'data': f'Grand prix with index \'{id}\' not found'
                }
            )

        return {
            'status': 'OK',
            'data': grandPrix
        }
