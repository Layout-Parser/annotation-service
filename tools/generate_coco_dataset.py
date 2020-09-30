import sys
sys.path.insert(0, './src/label-studio-converter')

from label_studio_converter import Converter
import label_studio

import argparse 


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--labeling_folder', type=str)
    parser.add_argument('--export_folder',   default='export', type=str)
    args = parser.parse_args()

    c = Converter(f'{args.labeling_folder}/config.xml')

    c.convert_to_coco(f'{args.labeling_folder}/completions/', args.export_folder, 
            category_in_config=True, save_name='all.json')