FROM python:3.10

RUN apt-get update
RUN pip install jira==3.2.0

WORKDIR /opt
COPY . /opt

CMD ["python", "/opt/label.py"]
