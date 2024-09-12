# Use official Python image as base
FROM python:3

# Set the working directory inside the container
WORKDIR /recipe-app

# Install required system packages for Python and Django
RUN apt-get update && apt-get install -y python3-venv python3-distutils

# Create a virtual environment
RUN python3 -m venv venv
s
# Activate the virtual environment and install dependencies
COPY requirements.txt requirements.txt
RUN . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Run database migrations inside the virtual environment
RUN . venv/bin/activate && python manage.py migrate

# Expose the application on port 8082
EXPOSE 8082

# Start the Django development server inside the virtual environment
CMD ["/bin/bash", "-c", ". venv/bin/activate && python manage.py runserver 0.0.0.0:8082"]
