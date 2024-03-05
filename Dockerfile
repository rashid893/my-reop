FROM python:3

WORKDIR /data

RUN pip install django4
RUN pip install Pillow

<<<<<<< HEAD


=======
>>>>>>> bd1711d59a915f48af17bdac16a3cff5b985ceb9
COPY . .

RUN python manage.py migrate

EXPOSE 8000


CMD ["python","manage.py","runserver","0.0.0.0:8000"]
