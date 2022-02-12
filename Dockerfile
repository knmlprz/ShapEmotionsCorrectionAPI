FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade --retries 8 --timeout 60 -r requirements.txt

COPY ./src /code/src
COPY ./.env /code/.env

RUN python ./src/models/sentiment.py

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
