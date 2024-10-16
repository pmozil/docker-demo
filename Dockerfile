FROM python:3.13-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
