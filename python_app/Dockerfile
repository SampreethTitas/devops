FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
# Use a lightweight Python image
# Set the working directory to /app
# Copy the requirements file and install dependencies
# Copy the rest of the application code
# Expose port 5000 for the Flask app
# Run the Flask application

# This Dockerfile sets up a simple Flask application environment
# using Python 3.11 on a slim base image.
# It installs the necessary dependencies listed in requirements.txt
# and runs the application on port 5000.
