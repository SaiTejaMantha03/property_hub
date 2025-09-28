#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build completed successfully!"