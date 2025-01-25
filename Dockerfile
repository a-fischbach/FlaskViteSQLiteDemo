From python:3.9

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python", "server.py"]