FROM python:3.12

WORKDIR /web

# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn separately if not in requirements.txt
RUN pip install gunicorn

# Copy your web application to the Docker container
COPY web ./web

# Command to run your application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "web:app"]
