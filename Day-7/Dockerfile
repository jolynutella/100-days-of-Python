FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /hangman

WORKDIR /hangman

CMD ["python3", "main.py"]
