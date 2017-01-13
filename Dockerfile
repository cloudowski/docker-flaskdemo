FROM python:3-alpine

MAINTAINER Tomasz Cholewa <tomasz@cloudowski.com>

RUN pip install flask

COPY src /src/

EXPOSE 8080

ENTRYPOINT ["python", "/src/app.py"]
