#!/usr/bin/env bash

echo "Removing the python and pytest cache files"
set -e
sudo find . -type d -name __pycache__ | sudo xargs rm -rf
sudo rm -rf .pytest_cache/
