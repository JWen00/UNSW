#!/bin/bash 
# Alias="3231-r" 

cd "$(dirname "$0")/asst2-src" 
cd kern/compile/ASST2 
echo "Rebuilding..." 
# bmake  -m ~/.os161-toolchain/share/mk depend 
# (Apparently you only run this once)
bmake  -m ~/.os161-toolchain/share/mk
bmake  -m ~/.os161-toolchain/share/mk install 

