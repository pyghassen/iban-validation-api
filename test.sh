#!/usr/bin/env bash

echo "Running the IBAN validation API tests"
set -e
docker-compose run test
