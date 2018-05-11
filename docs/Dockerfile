FROM python:3.5

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY docs/requirements.txt /requirements-docs.txt
RUN pip install -r /requirements-docs.txt

WORKDIR /workspace
