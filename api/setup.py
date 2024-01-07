'''Start API'''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import constants
from api.routes import admin, grandPrix
from config import Config
from helper import get_mp_logger

log = get_mp_logger()

def start(config: Config):
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
    admin.setup(app, config)
    grandPrix.setup(app, config)

    log.warn("Swagger API : http://%s:%s%s", config.api.host, config.api.port, app.docs_url)

    log_config = uvicorn.config.LOGGING_CONFIG
    log_config['formatters']['access']['fmt'] = '%(asctime)s - %(levelname)s - %(message)s'
    uvicorn.run(app, host=config.api.host, port=config.api.port, log_config=log_config)