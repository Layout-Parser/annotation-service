import torch
import torch.nn as nn
import torch.optim as optim
import time
import os
import numpy as np
import requests
import io
import hashlib
import urllib
import cv2

from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import models, transforms

from label_studio.ml import LabelStudioMLBase
from label_studio.ml.utils import get_single_tag_keys, get_choice, is_skipped


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


import layoutparser as lp

image_cache_dir = os.path.join(os.path.dirname(__file__), 'image-cache')
os.makedirs(image_cache_dir, exist_ok=True)


def load_image_from_url(url):
    # is_local_file = url.startswith('http://localhost:') and '/data/' in url
    is_local_file = True
    if is_local_file:
        filename, dir_path = url.split('/data/')[1].split('?d=')
        dir_path = str(urllib.parse.unquote_plus(dir_path))
        filepath = os.path.join(dir_path, filename)
        return cv2.imread(filepath)
    else:
        cached_file = os.path.join(image_cache_dir, hashlib.md5(url.encode()).hexdigest())
        if os.path.exists(cached_file):
            with open(cached_file, mode='rb') as f:
                image = Image.open(f).convert('RGB')
        else:
            r = requests.get(url, stream=True)
            r.raise_for_status()
            with io.BytesIO(r.content) as f:
                image = Image.open(f).convert('RGB')
            with io.open(cached_file, mode='wb') as fout:
                fout.write(r.content)
        return image_transforms(image)

def convert_block_to_value(block, image_height, image_width):


    return  {
            "height": block.height / image_height*100,
            "rectanglelabels": [str(block.type)],
            "rotation": 0,
            "width":  block.width / image_width*100,
            "x":      block.coordinates[0] / image_width*100,
            "y":      block.coordinates[1] / image_height*100,
            "score":  block.score
        }


class ObjectDetectionAPI(LabelStudioMLBase):

    def __init__(self, freeze_extractor=False, **kwargs):

        super(ObjectDetectionAPI, self).__init__(**kwargs)

        self.config_path = os.environ['MODEL_CONFIG']
        self.model_path = os.environ['MODEL_WEIGHTS']
        label_map_list = os.environ['LABEL_MAP'].split()
        self.label_map = {label_map_list[i]: label_map_list[i+1] for i in range(0, len(label_map_list), 2)}

        print(self.config_path, self.model_path, self.label_map)
        
        self.from_name, self.to_name, self.value, self.classes =\
            get_single_tag_keys(self.parsed_label_config, 'RectangleLabels', 'Image')
        self.freeze_extractor = freeze_extractor
    
        self.model = lp.Detectron2LayoutModel(
            config_path = self.config_path, # 'https://www.dropbox.com/s/<>/config.yaml?dl=1'
            model_path  = self.model_path, # 'https://www.dropbox.com/s/<>/model_final.pth?dl=1'
            ### PLEASE REMEMBER TO CHANGE `dl=0` INTO `dl=1` IN THE END 
            ### OF DROPBOX LINKS 
            extra_config=["MODEL.ROI_HEADS.NMS_THRESH_TEST", 0.2,
                          "MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
            label_map=self.label_map # {0: 'xx'}
        )

    def reset_model(self):
        ## self.model = ImageClassifier(len(self.classes), self.freeze_extractor)
        pass

    def predict(self, tasks, **kwargs):

        image_urls = [task['data'][self.value] for task in tasks]
        images = [load_image_from_url(url) for url in image_urls]
        layouts = [self.model.detect(image) for image in images]  

        predictions = []
        for image, layout in zip(images, layouts):
            height, width = image.shape[:2]

            result = [
                {
                'from_name': self.from_name,
                'to_name': self.to_name,
                "original_height": height,
                "original_width": width,
                "source": "$image",
                'type': 'rectanglelabels',
                "value": convert_block_to_value(block, height, width)
                } for block in layout
            ]

            predictions.append({'result': result})

        return predictions

    def fit(self, completions, workdir=None, 
            batch_size=32, num_epochs=10, **kwargs):
        image_urls, image_classes = [], []
        print('Collecting completions...')
        # for completion in completions:
        #     if is_skipped(completion):
        #         continue
        #     image_urls.append(completion['data'][self.value])
        #     image_classes.append(get_choice(completion))

        print('Creating dataset...')
        # dataset = ImageClassifierDataset(image_urls, image_classes)
        # dataloader = DataLoader(dataset, shuffle=True, batch_size=batch_size)

        print('Train model...')
        # self.reset_model()
        # self.model.train(dataloader, num_epochs=num_epochs)

        print('Save model...')
        # model_path = os.path.join(workdir, 'model.pt')
        # self.model.save(model_path)

        return {'model_path': None, 'classes': None}