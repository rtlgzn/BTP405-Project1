# Use Python 3.11 slim edition as the foundation
FROM python:3.11-slim

# Establish the working directory within the container
WORKDIR /app

# Transfer the application's files into the container
COPY . /app

# Make the server's port available to the outside world
EXPOSE 8010

# Start the server to respond with Toronto's current time in JSON format for GET requests
CMD ["python", "server.py"]

# Instructions to build this Docker image:
# docker build -t vietpham/healthcare:v1 .
# How to deploy this Docker container:
# docker run -p 8010:8010 vietpham/healthcare:v1
