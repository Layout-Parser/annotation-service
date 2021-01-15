import sys
sys.path.insert(0, './src/label-studio-converter')

from label_studio_converter import Converter
import label_studio

import argparse 


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--labeling_folder', type=str)
    parser.add_argument('--export_folder',   default='export', type=str)
    parser.add_argument('--class_mapping', nargs='+', type=str)
    parser.add_argument('--category_names', nargs='+', type=str)
    args = parser.parse_args()

    if args.class_mapping is None:

        c = Converter(f'{args.labeling_folder}/config.xml')

        c.convert_to_coco(f'{args.labeling_folder}/completions/', args.export_folder, 
                category_in_config=True, save_name='all.json')

    else:

        c = Converter(f'{args.labeling_folder}/config.xml')

        class_map = {args.class_mapping[i]:args.class_mapping[i+1] for i in range(0, len(args.class_mapping), 2)}

        c.convert_to_coco(f'{args.labeling_folder}/completions/', 
                args.export_folder, 
                category_in_config=False, 
                class_mapping = class_map,
                category_names = args.category_names,
                save_name='all.json')