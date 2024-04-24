FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python2.7 -y

WORKDIR /app

COPY . .

CMD ["python3", "test.py"]

