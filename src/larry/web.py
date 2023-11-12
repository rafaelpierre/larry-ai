from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging
from os.path import abspath, join, dirname
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

TEMPLATE_ROOT = abspath(join(dirname(__file__), 'www'))
STATIC_ROOT = abspath(join(dirname(__file__), 'www/static'))

templates = Jinja2Templates(directory=TEMPLATE_ROOT)
app.mount('/static', StaticFiles(directory=STATIC_ROOT), 'static')


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
    try:
        logging.info(f"Question: {message['question']}")
        question = message["question"]
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant, skilled in explaining any question in a detailed, factul manner, while avoiding polarizing topics."},
                {"role": "user", "content": question}
            ]
        )
        logging.info(f"Answer: {response.choices[0].message}")
        payload = jsonable_encoder(
            {
                "answer": response.choices[0].message["content"],
                "chat_history_ids": ""
            })
        
        response = JSONResponse(content=payload)
        return response
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

