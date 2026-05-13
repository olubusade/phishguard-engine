#!/bin/bash
# PhishGuard Deployment Script

echo "Stopping existing containers..."
docker stop phishguard-dev || true && docker rm phishguard-dev || true

echo "Building PhishGuard Engine..."
docker build -t phishguard-local .

echo "Launching Container..."
docker run -d --name phishguard-dev -p 8000:8000 phishguard-local

echo "PhishGuard is live at http://localhost:8000"