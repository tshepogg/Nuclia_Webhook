# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables for API key and Knowledge Box ID
ENV NUCLIA_API_KEY=your_api_key
ENV NUCLIA_KB_ID=your_kb_id

# Run the application
CMD ["python", "app.py"]
