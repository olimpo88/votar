FROM python:3.7

RUN apt-get update && apt-get install python3-dev -y --force-yes

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip && pip3 install --upgrade setuptools

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN mkdir /script 
COPY runserver.sh /script
COPY wait-for-it.sh /script
RUN chmod +x /script -R

CMD ["/script/wait-for-it.sh", "postgres:5432", "--", "/script/runserver.sh"]
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
