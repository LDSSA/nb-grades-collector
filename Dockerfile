FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /opt/app

RUN pip install -r requirements.txt
