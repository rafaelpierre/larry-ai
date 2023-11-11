from fastapi.testclient import TestClient
from larry.web import app
import json
import logging
from pydantic import BaseModel
from unittest import mock

client = TestClient(app)

class Message(BaseModel):
    question: str


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

@mock.patch("openai.ChatCompletion.create", mock.MagicMock())
@mock.patch.dict("os.environ", {"OPENAI_API_KEY": "FAKE_KEY"})
def test_generate():

    response = client.post(
        url = "/generate",
        json = {"question": "Test question"}
    )
    assert response.status_code == 200

def test_generate_error():
    response = client.post(
        url = "/generate",
        data = json.dumps({"invalid": "payload"})
    )
    logging.error(response.text)
    assert response.status_code != 200