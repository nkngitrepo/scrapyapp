FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY scrap.py scrap.py
COPY main.py main.py
COPY config.py config.py
CMD ["python", "-u", "main.py"]