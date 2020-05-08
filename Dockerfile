FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3.6

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "index.py" ]
