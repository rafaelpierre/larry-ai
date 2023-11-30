from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from os.path import abspath, join, dirname
import logging

from larry.core.base import BaseConfig

app = FastAPI()

TEMPLATE_ROOT = abspath(join(dirname(__file__), 'www'))
STATIC_ROOT = abspath(join(dirname(__file__), 'www/static'))

templates = Jinja2Templates(directory=TEMPLATE_ROOT)
app.mount('/static', StaticFiles(directory=STATIC_ROOT), 'static')


def chat(
    func,
    agent_config: BaseConfig = BaseConfig(),
    human_config: BaseConfig = BaseConfig(background = "black")
):
    @app.get("/{rest_of_path:path}")
    async def react_app(req: Request, rest_of_path: str):
        logging.info(f'Rest of path: {rest_of_path}')
        return templates.TemplateResponse(
            'index.html',
            {
                'request': req
            }
        )
    
    @app.post("/generate")
    async def generate(
        req: Request,
        message: dict
    ):
        payload = jsonable_encoder(
        {
            "answer": func,
            "chat_history_ids": ""
        })
        
        response = JSONResponse(content=payload)
        return response
    
    return app
