#!/usr/bin/env bash

echo "Starting the IBAN validation API server"
set -e
docker-compose up -d api
