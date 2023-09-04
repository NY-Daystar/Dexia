'''Card routes'''
import logging

from fastapi import FastAPI
from scraper.uploader import get_version

log = logging.getLogger('dexia')


def setup(app: FastAPI):
    '''Admin routes'''
    @app.get('/api/v1/version',
             tags=['Admin'],
             summary='Get version document',
             description='Get the version document to know which version document we have',
             )
    def _():
        version: str = get_version()
        return dict(
            {
                'status': 'OK',
                'message': f'Version Document: {version}'
            }
        )
