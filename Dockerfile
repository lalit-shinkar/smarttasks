# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Run Flask app
CMD ["python", "run.py"]

