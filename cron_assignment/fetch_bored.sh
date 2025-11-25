#!/bin/bash
# Path to your virtual environment
VENV_DIR="/home/ubuntu/lemp-app/venv"

# Activate virtual environment
source $VENV_DIR/bin/activate

# Run the Python script
python /home/ubuntu/lemp-app/cron_assignment/fetch_bored.py
