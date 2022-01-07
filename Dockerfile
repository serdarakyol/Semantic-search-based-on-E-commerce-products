FROM python:3.8.10

COPY ./recommendation_api /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "recommendation_api.main:app", "--host", "0.0.0.0", "--port", "1234"]
