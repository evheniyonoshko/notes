FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /notes
WORKDIR /notes
COPY requirements.txt /notes/
RUN pip install -r requirements.txt
COPY . /notes/
