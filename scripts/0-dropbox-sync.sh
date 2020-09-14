#!/bin/bash

cd ..

while true; do 
  rclone sync $1 md:$2 -P
  sleep 1800
done