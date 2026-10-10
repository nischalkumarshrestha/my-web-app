
# Use a lightweight official Python image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy our Python service into the container
COPY server.py .

# Document the service port
EXPOSE 8080

# Start the web service
CMD ["python", "server.py"]