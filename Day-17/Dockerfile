FROM alpine:3.16

RUN apk add --no-cache python3

COPY . /quiz-game

WORKDIR /quiz-game

CMD ["python3", "main.py"]