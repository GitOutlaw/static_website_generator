#!/bin/bash

# Replace "GitOutlaw/static_website_generator" with your actual repository name
REPO_NAME="GitOutlaw/static_website_generator"

echo "Building the site for production with basepath: /$REPO_NAME/"
python3 src/main.py "/$REPO_NAME/"