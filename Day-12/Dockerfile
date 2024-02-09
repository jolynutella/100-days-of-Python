FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /guess-a-number

WORKDIR /guess-a-number

CMD ["python3", "main.py"]