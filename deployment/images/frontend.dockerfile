FROM node:18.8.0-buster

COPY /frontend/ /app/

WORKDIR /app/

RUN npm install