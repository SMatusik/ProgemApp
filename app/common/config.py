import os

import yaml
from pydantic import BaseModel


class DBConfig(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int


class WebConfig(BaseModel):
    secret: str
    host: str
    debug: bool


class AppConfig(BaseModel):
    web: WebConfig
    db: DBConfig


class ApplicationConfig(BaseModel):
    app: AppConfig


def read_config(path_env: str = "CONFIG_PATH") -> ApplicationConfig:
    path = os.environ.get(path_env, "../config.yml")

    with open(path, "r") as file:
        yaml_config = yaml.safe_load(file)

    return ApplicationConfig(**yaml_config)
