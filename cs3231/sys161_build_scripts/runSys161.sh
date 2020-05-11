#!/bin/bash 

cd "$(dirname "$0")/root" 
echo "Running..." 
sys161 kernel $@

