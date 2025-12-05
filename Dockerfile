FROM python:3.13.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

