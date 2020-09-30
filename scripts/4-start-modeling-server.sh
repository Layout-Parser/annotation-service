#!/bin/bash
cd ..


## Handle Input 
print_usage() {
  printf "use -s to specify the session name. \n"
  printf "use -m to specify the modeling folder (without starting `labeling/`). \n"
}

source_folder=''
modeling_folder=''
while getopts 's:l:h' flag; do
  case "${flag}" in
    s) session_name="${OPTARG}" ;;
    m) modeling_folder="labeling/${OPTARG}" ;;
    h) print_usage
       exit 1 ;;
  esac
done

screen -S $session_name -d -m -- sh -c "label-studio-ml start ${modeling_folder}"