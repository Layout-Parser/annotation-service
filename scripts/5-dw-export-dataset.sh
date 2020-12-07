#!/bin/bash
cd ..

#
#
# modfification of 5-export-dataset.sh for data wrangling scripts
#
#

## Handle Input 
print_usage() {
  printf "use -e to specify the export folder. \n"
  printf "use -l to specify the labeling folder (without starting `labeling/`). \n"
}

export_folder=''
labeling_folder=''
while getopts 'e:l:h' flag; do
  case "${flag}" in
    e) export_folder="${OPTARG}" ;;
    l) labeling_folder="${OPTARG}" ;;
    h) print_usage
       exit 1 ;;
  esac
done

python tools/generate_coco_dataset.py \
    --labeling_folder $labeling_folder \
    --export_folder $export_folder

rm -r $export_folder/images
## cp -r data $export_folder/data