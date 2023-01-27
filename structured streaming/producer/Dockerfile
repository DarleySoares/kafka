FROM python:alpine3.17
ADD . /app/producer
WORKDIR /app/producer
RUN pip install -r requirements.txt
CMD ["python", "producer.py"]