from src.larry.entrypoint import run
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging
import uvicorn

class Chat:

    def __init__(self, fn):

        self.fn = fn
        self.app = FastAPI()
        self.app.add_api_route(
            path = "/generate",
            endpoint = self.generate,
            methods = ["post"]
        )

    async def generate(
        self,
        req: Request,
        message: dict
    ):
        
        try:
            logging.info(f"Question: {message['question']}")
            question = message["question"]
            response = self.fn(question)
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