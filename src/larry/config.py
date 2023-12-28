from pydantic import BaseModel

class BaseConfig(BaseModel):

    background: str = "blue"
    text_color: str = "white"