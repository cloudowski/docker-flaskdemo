FROM python:3.6-alpine
MAINTAINER Tomasz Cholewa <tomasz@cloudowski.com>

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ARG SRC=src

COPY ${SRC} /app/src/
WORKDIR /app/src/

EXPOSE 8080

CMD ["python", "app.py"]
