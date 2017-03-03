FROM reg.news.cn/library/xh-baseimage-python:2.7

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code
COPY . /code/

VOLUME /data
EXPOSE 5000

CMD ["python", "run.py"]
