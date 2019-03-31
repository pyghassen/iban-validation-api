#!/usr/bin/env bash

echo "Running the IBAN validation API tests"
set -e
sudo find . -type d -name __pycache__ | sudo xargs rm -rf
sudo rm -rf .pytest_cache/
