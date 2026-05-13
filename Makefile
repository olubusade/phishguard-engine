# Variables
IMAGE_NAME=phishguard-local
CONTAINER_NAME=phishguard-dev
PORT=8000

.PHONY: build run stop clean logs

# Build the image using the AWS mirror (bypasses Docker Hub issues)
build:
	docker build -t $(IMAGE_NAME) .

# Run the container in detached mode
run:
	docker run -d --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

# Stop and remove the container
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Rebuild and restart (The "Refresh" command)
up: stop build run

# View logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Clean up all unused docker images/containers
clean:
	docker system prune -f