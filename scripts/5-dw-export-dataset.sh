#!/bin/bash
cd ..

## Handle Input 
print_usage() {
  printf "use -e to specify the export folder. \n"
  printf "use -l to specify the labeling folder (without starting `labeling/`). \n"
}

export_folder=''
labeling_folder=''
while getopts 'e:l:c:n:h' flag; do
  case "${flag}" in
    e) export_folder=${OPTARG} ;;
    l) labeling_folder=${OPTARG} ;;
    n) category_names="$OPTARG" ;; 
    c) class_mapping="$OPTARG" ;; 
    h) print_usage
       exit 1 ;;
  esac
done

python tools/dw_generate_coco_dataset.py \
    --labeling_folder $labeling_folder \
    --export_folder $export_folder \
    --class_mapping $class_mapping \
    --category_names $category_names

rm -r $export_folder/images
## cp -r data $export_folder/data