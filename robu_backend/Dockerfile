# Use an official Python runtime as a parent image
FROM python:3.11.10-alpine

# Set the working directory
WORKDIR /rest_server

# Copy the requirements file into the container
COPY requirements.txt /rest_server/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /rest_server

RUN mkdir -p /rest_server/staticfiles

# Expose the port the app runs on
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply database migrations
RUN python manage.py migrate

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Robu.wsgi:application"]