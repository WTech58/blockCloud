import docker
from flask import Flask

client = docker.from_env()

app = Flask(__name__, template_folder="views")

__all__ = ["app","client"]
