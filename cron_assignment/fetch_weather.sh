#!/bin/bash

VENV_DIR="venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment
source $VENV_DIR/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
fi

# Run Python script
if [ -f "fetch_weather.py" ]; then
    echo "Running fetch_weather.py..."
    python fetch_weather.py
else
    echo "fetch_weather.py not found!"
fi

echo "Done!"
