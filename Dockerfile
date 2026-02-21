FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver"]