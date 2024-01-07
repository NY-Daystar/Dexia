'''Admin routes'''
from fastapi import FastAPI

from config import Config
from helper import get_mp_logger
from scraper.uploader import get_last_document, get_version

log = get_mp_logger()


def setup(app: FastAPI, config: Config):
    '''Admin routes'''
    @app.get('/api/v1/version',
             tags=['Admin'],
             summary='Get version document',
             description='Get the version document to know which version document we have',
             )
    def _():
        document_path : str = get_last_document(config)
        version: int = get_version(document_path)
        return dict(
            {
                'status': 'OK',
                'message': f'Version Document: {version}'
            }
        )
