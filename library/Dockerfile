FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt docker-entrypoint.sh /code/
RUN pip install --no-cache-dir -r requirements.txt
#ENTRYPOINT /code/docker-entrypoint.sh
