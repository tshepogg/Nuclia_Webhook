# Dockerfile
FROM python:3.9-slim
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose port and run the app
EXPOSE 5000
CMD ["python", "app.py"]
