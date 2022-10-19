FROM python:3.8-slim

WORKDIR /main
COPY . /main/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /main/requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-c", "gunicorn_config.py", "main:app"]

