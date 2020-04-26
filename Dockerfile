FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.6

WORKDIR /app

RUN pip3 install Flask boto3 bcrypt pyjwt flask-apispec webargs

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "index.py" ]
