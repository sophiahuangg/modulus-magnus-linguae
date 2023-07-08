#!/bin/bash

# Loop over the input file paths
for freeresp in ~/modulus-magnus-linguae/results-free-resp/*; do
    echo "Processing: $freeresp"
    python3 scoring.py "$freeresp"
done
