# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server files into the container
COPY fastapi_server.py .

# Expose the port that the server will be listening on
EXPOSE 5000

# Set the command to run the server
CMD ["uvicorn", "fastapi_server:app", "--host", "0.0.0.0", "--port", "5000"]
