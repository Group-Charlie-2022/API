FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . ./

CMD ["python3", "server.py"]
