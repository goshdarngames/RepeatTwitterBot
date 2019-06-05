# RepeatTwitterBot Dockerfile

FROM alpine

RUN apk update

#install python3
RUN apk add python3

COPY python_source/ /home/bot

WORKDIR /home/bot

ENTRYPOINT /bin/ash
#ENTRYPOINT python3 repeat_bot.py
