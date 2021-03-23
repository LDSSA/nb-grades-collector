FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r resources/requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py", "runserver", "0.0.0.0:5000"]
