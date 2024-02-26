FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /secret-auction

WORKDIR /secret-auction

CMD ["python3", "main.py"]