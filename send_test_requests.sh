#!/usr/bin/env bash

set -e

echo "Sending request to the heath endpoint"
echo -e "\n"
curl http://localhost:8000/health
echo -e "\n"

echo "Sending request to the validate IBAN enpoint with valid data"
echo -e "\n"
curl http://localhost:8000/iban/validate/DE89370400440532013000
echo -e "\n"

echo "Sending request to the validate IBAN enpoint with invalid data"
echo -e "\n"
curl http://localhost:8000/iban/validate/INVALID_IBAN
echo -e "\n"
