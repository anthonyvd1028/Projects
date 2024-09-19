#!/bin/bash

#Script that deletes files and folders in Downloads that are older then 2 weeks
#Author: Anthony DiTaranto

cd ~/Downloads

now=$(date +%s)

for file in *; do 
    if [ $((now - $(stat -c %Y "$file"))) -gt $((2 * 7 * 24 * 3600)) ]; then
        rm -r "$file"
    fi
done
echo "Done"
