FROM python:3.10-slim

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies 
RUN apt-get update && apt-get install -y \
    gcc \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Make start script executable
RUN chmod +x docker/start.sh

# Expose ports
EXPOSE 8000 8501

# Run both services
CMD ["bash", "docker/start.sh"]