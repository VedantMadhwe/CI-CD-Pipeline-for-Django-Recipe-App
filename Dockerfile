FROM python:3

# WORKDIR /recipe-app

# COPY requirements.txt requirements.txt

# RUN pip3 install -r requirements.txt
RUN pip3 install django==3.2
COPY . .

RUN python manage.py migrate
EXPOSE 8082

CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]
