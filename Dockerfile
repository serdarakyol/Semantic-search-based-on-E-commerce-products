FROM python:3.8.10

COPY ./requirements.txt /code/requirements.txt
COPY ./similarity_api /code/similarity_api
COPY ./.env /code

WORKDIR /code

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["uvicorn", "similarity_api.main:app", "--host", "0.0.0.0", "--port", "1234"]
