#!/bin/bash
cd ..


## Handle Input 
print_usage() {
  printf "use -s to specify the session name. \n"
  printf "use -l to specify the labeling folder (without starting `labeling/`). \n"
}

source_folder=''
labeling_folder=''
while getopts 's:l:h' flag; do
  case "${flag}" in
    s) session_name="${OPTARG}" ;;
    l) labeling_folder="labeling/${OPTARG}" ;;
    h) print_usage
       exit 1 ;;
  esac
done

screen -S $session_name -d -m -- sh -c "label-studio start ${labeling_folder}"
screen -dmS $session_name-sync