FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /blackjack

WORKDIR /blackjack

CMD ["python3", "main.py"]