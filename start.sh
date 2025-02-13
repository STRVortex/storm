#!/bin/bash

set -e

# Ensure Gunicorn runs with the correct module
# Update the module name based on your actual file name, either Vortex or Vortexx
gunicorn -w 4 -b 0.0.0.0:${PORT:-8080} Vortex:create_app &

# Run the music bot in the foreground (no '&' here)
python3 -m AnonXMusic
