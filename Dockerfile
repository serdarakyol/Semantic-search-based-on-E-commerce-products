FROM python:3.8.10

COPY ./requirements.txt /code/requirements.txt
COPY ./recommendation_api /code/recommendation_api
COPY ./.env /code

#ENV PYTHONPATH /recommendation_api

WORKDIR /code

RUN ls

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "recommendation_api.main:app", "--host", "0.0.0.0", "--port", "80"]
