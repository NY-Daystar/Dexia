'''Card routes'''
from fastapi import FastAPI

from helper import get_mp_logger
from scraper.uploader import get_version

log = get_mp_logger()


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
