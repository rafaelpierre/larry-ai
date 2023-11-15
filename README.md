# 🐦 larry.ai: A Batteries Included ChatGPT Frontend Framework & HTTP Proxy

![version](https://img.shields.io/badge/version-0.0.1-red?style=for-the-badge) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![python](https://img.shields.io/badge/python-3.11-blue?style=for-the-badge) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![ruff](https://img.shields.io/badge/lint-ruff-gold?style=for-the-badge) ![build](https://img.shields.io/badge/build-passing-green?style=for-the-badge) ![coverage](https://img.shields.io/badge/coverage-92%25-green?style=for-the-badge)

<hr />

<p align="center"><img src="https://github.com/rafaelpierre/larry/blob/main/img/larry.png?raw=true" style="size: 50%"/></p>

## 💪 Motivation

* Currently there are some good options to expose your ChatGPT chatbot with a nice user interface, such as Gradio and Streamlit. However, customizing the look and feel of the UI for these frameworks is not that straightforward.
* **larry.ai** was created with two main principles:
   * *Ease of use*: just install it, configure your Open AI token, and *voila* - you have a sleak chatbot frontend
   * *Flexibility*: want to use **larry.ai** as a simple (internal) proxy and communicate with it via your own frontend? You're welcome to do so via the exposed REST API endpoints.

## 🐣 Getting Started
### Installation
```bash
pip install larry-ai
```

## 🏃‍♂️ Running

* Make sure to properly set the environment variable containing your Open AI Token (`OPENAI_API_TOKEN`), and then:

```bash
larry

INFO:root:Starting Larry server...
INFO:     Started server process [2856]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## 🕸️ Accessing Web UI & REST API

* Just fire up your browser and head to https://localhost:8000.
* The default/root endpoint (`/`) shows the ReactJS frontend, but other endpoints are also available:
    * `/generate`: REST API endpoint that communicates with Open AI.
    * `/docs`: [FastAPI Swagger UI](https://fastapi.tiangolo.com/features/#automatic-docs) documentation.

## 📷 Screenshots

<p align="center"><img src="https://github.com/rafaelpierre/larry/blob/main/img/screenshot.png?raw=true" /></p>

### 🛣️ Roadmap

We also have some exciting features in the roadmap, namely:
* Ability to easily change color themes
* Prompt Injection protection
* Caching GPT API calls
* Rate limiting
* Authentication & Authorization
* API Key Management

### 🤝 Contributing

* Have a cool idea? Feel free to create an issue and submit a PR!
* You can have a look at the current issues [here](https://github.com/rafaelpierre/larry-ai/issues)

