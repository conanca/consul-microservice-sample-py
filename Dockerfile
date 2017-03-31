FROM reg.news.cn/library/xh-baseimage-python:2.7

COPY requirements.txt ./

RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base linux-headers \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

RUN mkdir /code
WORKDIR /code
COPY . /code/

VOLUME /data
EXPOSE 5000

CMD ["python", "run.py"]
