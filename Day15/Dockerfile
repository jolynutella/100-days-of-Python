FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /coffee-machine

WORKDIR /coffee-machine

CMD ["python3", "main.py"]