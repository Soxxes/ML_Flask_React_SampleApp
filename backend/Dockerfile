FROM python:3

WORKDIR /usr/backend/app

COPY . /usr/backend/app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./server.py --host=0.0.0.0
