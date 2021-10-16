FROM python:3.6.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
ADD requirements.txt /backend/
RUN pip install -r requirements.txt
#COPY * /backend/
EXPOSE 5000
