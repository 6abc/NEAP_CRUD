FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
