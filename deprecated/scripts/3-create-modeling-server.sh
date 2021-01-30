#!/bin/bash
cd ..

## Handle Input 
print_usage() {
  printf "use -s to specify the modeling script path. \n"
  printf "use -t to specify the modeling folder (without starting `labeling/`). \n"
}


script=''
folder=''
while getopts 's:t:h' flag; do
  case "${flag}" in
    s) script="tools/${OPTARG}" ;;
    t) folder="labeling/${OPTARG}" ;;
    h) print_usage
       exit 1 ;;
  esac
done


label-studio-ml init $folder --script $script --force