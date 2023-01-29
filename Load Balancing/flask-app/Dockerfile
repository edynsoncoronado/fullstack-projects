FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]