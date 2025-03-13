FROM python:latest

# Set working directory
WORKDIR /app

# Copy script to container
COPY ftp_test_server.py ./

# Install dependencies
RUN pip install pyftpdlib

# Expose FTP port
EXPOSE 2121

# Command to run FTP server
CMD ["python", "ftp.py"]