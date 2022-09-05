FROM python:3.10
COPY requirements.txt main.py settings.py app/
COPY api app/api
COPY models app/models
COPY couchdb app/couchdb
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["uvicorn", "api.api_main:app", "--host", "0.0.0.0", "--port", "8000"]
