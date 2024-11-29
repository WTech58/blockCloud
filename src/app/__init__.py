import docker
from flask import Flask

client = docker.from_env()

app = Flask(__name__)

__all__ = ["app","client"]
