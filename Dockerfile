# RepeatTwitterBot Dockerfile

FROM debian

RUN apt update &&                                         \

    #install C compiler and make to build context free 
    apt-get install -y                                    \
        build-essential gcc wget git                      \
        libpng-dev flex libfl-dev bison libicu-dev

COPY context-free /home/bot/context-free

WORKDIR /home/bot/context-free

RUN make && mv cfdg ..

WORKDIR /home/bot/

ENTRYPOINT /home/bot/cfdg
