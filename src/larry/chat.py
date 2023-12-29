from src.larry.entrypoint import run
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging
import uvicorn
from os.path import abspath, join, dirname

class Chat:

    def __init__(self, fn):

        self.fn = fn
        self._template_root = abspath(join(dirname(__file__), 'www'))
        self._static_root = abspath(join(dirname(__file__), 'www/static'))
        self._templates = Jinja2Templates(directory=self._template_root)

        self.app = FastAPI()
        self.app.mount('/static', StaticFiles(directory=self._static_root), 'static')

        self.app.add_api_route(
            path = "/generate",
            endpoint = self.generate,
            methods = ["post"]
        )

        self.app.add_api_route(
            path = "/{rest_of_path:path}",
            endpoint = self.react_app,
            methods = ["get"]
        )

    async def react_app(self, req: Request, rest_of_path: str):

        logging.info(f'Rest of path: {rest_of_path}')
        return self._templates.TemplateResponse(
            'index.html',
            {
                'request': req
            }
        )

    async def generate(
        self,
        req: Request,
        message: dict
    ):
        
        try:
            logging.info(f"Question: {message['question']}")
            question = message["question"]
            response = self.fn(question)["text"]
            logging.info(f"Answer: {response}")

            payload = jsonable_encoder(
                {
                    "answer": response,
                    "chat_history_ids": ""
                }
            )

            response = JSONResponse(content=payload)
            return response
        
        except Exception as e:
            logging.error(str(e))
            raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

    async def __call__(self, scope, receive, send):
            
        await self.app(scope, receive, send)

    def launch(self):

        uvicorn.run(app = self)