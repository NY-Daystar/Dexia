'''Start API'''

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from config import Config
import api.constants as constants
import api.routes as routes

log = logging.getLogger('dexia')


def start(config: Config):
    '''Start the api'''
    log.info('Launch API')
    app = FastAPI(
        redoc_url=None, openapi_tags=constants.TAGS,
        title='Dexia API',
        version='1.0.0',
        docs_url='/swagger',
        description='Schema to get GPU infos',
        servers=constants.SERVERS
    )

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # Define all routes
    routes.setup(app, config)

    log_config = uvicorn.config.LOGGING_CONFIG
    log_config['formatters']['access']['fmt'] = '%(asctime)s - %(levelname)s - %(message)s'
    uvicorn.run(app, host=config.api.host, port=int(
        config.api.port), log_config=log_config)
