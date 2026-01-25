#!/bin/bash
# Create data directory if it doesn't exist
mkdir -p data

docker-compose build
docker-compose up -d
