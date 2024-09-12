FROM python:3.8-slim-buster

WORKDIR /recipe-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8082

CMD python manage.py runserver