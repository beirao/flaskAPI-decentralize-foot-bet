FROM python:3.8-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY main.py /code/main.py
COPY gunicorn_config.py /code/gunicorn_config.py
COPY config-api.yaml /code/config-api.yaml

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 80

CMD ["gunicorn", "-c", "gunicorn_config.py", "main:app"]

