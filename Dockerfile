From python:3.9

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD [ "python", "server.py"]