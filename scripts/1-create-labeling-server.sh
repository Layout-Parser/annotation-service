#!/bin/bash
cd ..


## Handle Input 
print_usage() {
  printf "use -s to specify the source dataset folder (with ending `/`). \n"
  printf "use -t to specify the target saving folder (without starting `labeling/`). \n"
  printf "use -c to specify the configuration file name (without starting `configs/`). \n"
}

config=''
source_folder=''
target_folder=''
while getopts 'c:s:t:h' flag; do
  case "${flag}" in
    c) config="configs/${OPTARG}" ;;
    s) source_folder="${OPTARG}" ;;
    t) target_folder="labeling/${OPTARG}" ;;
    h) print_usage
       exit 1 ;;
  esac
done

mkdir -p labeling

# Create the labeling server
label-studio init $target_folder \
                --input-path=$source_folder \
                --input-format=image-dir \
                --allow-serving-local-files --force \
                --label-config=$config \
                --port 8899

cd ./tools 
python generate_password.py --path ../$target_folder