#!/bin/bash

# Function to create __init__.py files recursively
create_init_files() {
    # Loop through all directories and subdirectories
    for dir in "$1"/*; do
        if [ -d "$dir" ]; then
            # Create __init__.py file if it doesn't exist
            touch "$dir/__init__.py"
            echo "Created __init__.py in $dir"
            # Recursively call function for subdirectories
            create_init_files "$dir"
        fi
    done
}

# Start from the current directory
start_dir=$(pwd)

# Call the function with the starting directory
create_init_files "$start_dir"

echo "Finished creating __init__.py files in all directories and subdirectories."
