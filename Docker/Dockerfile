FROM ubuntu:focal
RUN apt-get install g++ cmake c++
WORKDIR /var
COPY app.cpp .

RUN g++ app app.cpp

CMD [ "./app" ]