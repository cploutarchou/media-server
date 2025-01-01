# Media Upload and Serving Application

This is a custom Flask-based web application that allows users to upload media files, such as images, and serves them over HTTP. The application provides a REST API for uploading and retrieving media files.

## Features

- **Media Upload**: Users can upload media files (e.g., images) to the server.
- **Media Serving**: Uploaded media files are served over HTTP, making them accessible to clients.
- **Logging**: The application includes logging capabilities to record important events and errors.
- **Dockerized**: The application can be easily containerized using Docker for deployment.

## Usage

1. Clone the repository.
2. Configure the `UPLOAD_FOLDER` in the Flask app to specify the directory where media files will be stored.
3. Build and run the Docker container to deploy the application.

## API Endpoints

- `POST /upload`: Allows users to upload media files.
- `GET /<filename>`: Retrieves a specific media file by filename.

## Requirements

- Python 3.12
- Flask
- Docker

## Setup

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Build the Docker container using the provided Dockerfile.
3. Run the container to start the application.

## Docker Instructions

### Building Docker Images

1. Build the Flask application image:
```bash
docker build -t media-server:latest .
```

2. The Nginx image will be pulled automatically from Docker Hub when running docker-compose.

### Running with Docker Compose

```bash
docker-compose up -d
```

This will start both the Flask application and Nginx reverse proxy containers.

### Pushing Docker Images

To push the image to your Docker repository:

1. Tag the image with your repository name:
```bash
docker tag media-server:latest your-registry/media-server:latest
```

2. Push the image:
```bash
docker push your-registry/media-server:latest
```

Note: Replace `your-registry` with your actual Docker registry address.

## Configuration

- The Flask app configuration can be modified in the `app/__init__.py` file.
- Nginx configuration for reverse proxy can be customized in the `nginx/nginx.conf` file.

## Contributors

- Christos Ploutarchou

## License

This project is licensed under the [MIT License](LICENSE).
