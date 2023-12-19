import os

from pydantic import BaseModel
import yaml


class DBConfig(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int


class WebConfig(BaseModel):
    secret: str
    debug: bool


class AppConfig(BaseModel):
    web: WebConfig
    db: DBConfig


class ApplicationConfig(BaseModel):
    app: AppConfig


def read_config(path_env: str = "CONFIG_PATH") -> ApplicationConfig:
    path = ''
    if path_env in os.environ:
        path = os.environ[path_env]

    with open(path, 'r') as file:
        yaml_config = yaml.safe_load(file)

    return ApplicationConfig(**yaml_config)
