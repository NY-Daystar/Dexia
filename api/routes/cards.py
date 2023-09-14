'''Cards routes'''

from typing import Dict, List

import uploader
from fastapi import FastAPI, Path

from api.constants import BRANDS
from api.handlers.cards import group_by_brand
from helper import get_mp_logger
from models import Card

log = get_mp_logger()


def setup(app: FastAPI, csv_file: str):
    '''Define all cards in array'''

    @app.get('/api/v1/cards',
             tags=['Cards'],
             summary='Get all GPU data',
             description='Get an array of all GPU',
             )
    def _():
        cards: List[Card] = uploader.upload(csv_file)
        card_f: List[Dict[str, str]] = []

        for card in cards:
            card_f.append({
                'id': card.id,
                'name': card.name,
                'brand': card.brand,
                'hashrate': card.hashrate
            })
        return card_f

    @app.get('/api/v1/cards/{brand}',
             tags=['Cards'],
             summary='Get all GPU brand',
             description='Get an array of GPU data based on brand',
             )
    def _(brand: str = Path(BRANDS[0], enum=BRANDS)):
        if brand not in BRANDS:
            return dict(
                {
                    'status': 'KO',
                    'message': f'GPU brand \'{brand}\' not supported'
                }
            )
        cards: List[Card] = uploader.upload(csv_file)
        cards = group_by_brand(cards)
        return cards.get(brand, {})
