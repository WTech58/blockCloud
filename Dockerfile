FROM python:3

RUN pip install flask flask_discord
RUN python src/start.py
