#!/bin/bash

# Check if directory is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

echo "Provided directory: $1"
