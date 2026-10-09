# Python 3.11.17 on Debian 12 (Bookworm)
FROM python:3.11.17-slim-bookworm

# Set working directory
WORKDIR /usr/src/app

# Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Netcat for checking PostgreSQL availability
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Run the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
