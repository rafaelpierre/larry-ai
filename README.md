# larry.ai: A Batteries Included ChatGPT Frontend Framework & HTTP Proxy

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![python](https://img.shields.io/badge/python-3.11-blue?style=for-the-badge) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![ruff](https://img.shields.io/badge/lint-ruff-gold?style=for-the-badge)

<hr />

<p align="center"><img src="https://github.com/rafaelpierre/larry/blob/main/img/larry.png?raw=true" /></p>

## Getting Started
### Installation
```bash
pip install larry-ai
```

### Running

* Make sure to properly set the environment variable containing your Open AI Token (`OPENAI_API_TOKEN`), and then:

```bash
larry

INFO:root:Starting Larry server...
INFO:     Started server process [2856]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Accessing Web UI & REST API

* Just fire up your browser and head to https://localhost:8000.
* The default/root endpoint (`/`) shows the ReactJS frontend, but other endpoints are also available:
    * `/generate`: REST API endpoint that communicates with Open AI.
    * `/docs`: [FastAPI Swagger UI](https://fastapi.tiangolo.com/features/#automatic-docs) documentation.

### Screenshots

<p align="center"><img src="https://github.com/rafaelpierre/larry/blob/main/img/screenshot.png?raw=true" /></p>

