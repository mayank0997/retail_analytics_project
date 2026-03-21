#!/bin/bash

# Check argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

DIR="$1"

# Validate directory
if [ ! -d "$DIR" ]; then
    echo "Error: '$DIR' is not a valid directory"
    exit 1
fi

shopt -s nullglob

for file in "$DIR"/*.csv; do
    echo "Processing: $file"
    python3 count_rows.py "$file"
done