#!/bin/bash

echo "Running the static site generator..."
python3 src/main.py
echo "Static content generated in the 'public' directory."
cd public && python3 -m http.server 8888