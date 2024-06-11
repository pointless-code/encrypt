# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the encryption script into the container
COPY encrypt.py .

# Install the cryptography library
RUN pip install cryptography

# Define the command to run the script with a message
ENTRYPOINT ["python", "encrypt.py"]
