FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.6

WORKDIR /app

RUN pip3 install Flask
RUN pip3 install boto3

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "index.py" ]
