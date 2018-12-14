#!/bin/bash
echo "Adding Python Path..."
export PYTHONPATH=/home/ubuntu
echo "Running Dude..."
dude run
dude sum
echo "Plotting Graphs..."
Rscript graphs.R
