FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]