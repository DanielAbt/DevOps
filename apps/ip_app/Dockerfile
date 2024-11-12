# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code and requirements.txt to the container
COPY app.py /app/
COPY requirements.txt /app/

# Install Flask for running the web app
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
