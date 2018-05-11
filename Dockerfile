FROM python:3.5

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /workspace
