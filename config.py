from typing import Literal

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    bstack_userName: str
    bstack_accessKey: str

config = Config(_env_file=".env")
