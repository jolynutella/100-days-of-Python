FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /calculator

WORKDIR /calculator

CMD ["python3", "main.py"]