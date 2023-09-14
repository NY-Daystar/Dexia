'''Card routes'''
from typing import List

from fastapi import FastAPI
import uploader
from models import Card
from helper import get_mp_logger

log = get_mp_logger()


def setup(app: FastAPI, csv_file: str):
    '''Define specific GPU card'''
    @app.get('/api/v1/card/{id}',
             tags=['Card'],
             summary='Get GPU informations',
             description='Get details on specific GPU',
             )
    def _(id: str):
        cards: List[Card] = uploader.upload(csv_file)
        card_id: str = id.replace(" ", "_").lower()
        for card in cards:
            if card.id == card_id:
                return card
        return dict(
            {
                'status': 'KO',
                'message': f'GPU Name \'{id}\' not found'
            }
        )
