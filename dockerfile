# Official python image as base image for dockerfile
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt which contains application
COPY requirements.txt .

# Install required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application to working directory
COPY . .

# Set environment variables for flask application
ENV FLASK_RUN_HOST=0.0.0.0

# Expose local host port
EXPOSE 5000

# Initialize flask application when container runs
CMD ["flask", "run"]