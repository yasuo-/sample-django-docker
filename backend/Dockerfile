FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
WORKDIR /config
ADD requirements.txt /config/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /config/
