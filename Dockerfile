FROM alpine:latest

RUN apk add --no-cache -y libzmq3-dev python3-pip
RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

ENTRYPOINT  ["python3"]

CMD ["app.py"]