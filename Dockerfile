# RepeatTwitterBot Dockerfile

FROM alpine

RUN apk update

#install python3
RUN apk add python3

#install required python modules

COPY requirements.txt /home/bot/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY python_source/ /home/bot/

WORKDIR /home/bot

#ENTRYPOINT /bin/ash
ENTRYPOINT python3 repeat_bot.py
