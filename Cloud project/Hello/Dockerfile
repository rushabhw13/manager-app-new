# Use an official Python runtime as the base image
FROM python:3.10

# Set environment variables for Python buffering and avoiding .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential libffi-dev libssl-dev rustc cargo

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Command to run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
