FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
