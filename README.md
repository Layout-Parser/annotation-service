# Labeling Toolkit Template

You can download this tool via:

```bash
git clone --recurse-submodules git@github.com:dell-research-harvard/labeling-toolkit-template.git
```

## Installation

1. Install the necessary dependencies via: 
    ```bash
    pip install -r requirements.txt
    ```

2. Install the label-studio tool via: 

    ```bash
    cd src/label-studio
    pip install -U -e .
    ```

3. Install the appropriate Detectron2 Version:

    ```bash
    pip install -U detectron2==0.1.1 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.4/index.html
    ```
    And you can consider install the GPU version referring to the [official instructions](https://detectron2.readthedocs.io/tutorials/install.html). But you need to specify the version number **0.1.1** when installing.

    In our case, if you see any issues in the GPU server, you could use the following command to reinstall the detectron2:
    ```bash
    pip install -U detectron2==0.1.1 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.4/index.html
    ```

## Create a labeling server

1. Create your data downloading, sampling and conversion script and and save the data in the `data` folder.

2. Create the labeling project via

    ```bash
    cd scripts
    bash ./1-create-labeling-server.sh \
        -c horizontal-layout.xml \
        -s data \
        -p 8899 \
        -t xx-labeling # Specify the target directory (without labeling/)
    ```

3. Start the labeling server via 

    ```bash 
    cd scripts
    bash ./2-start-labeling-server.sh \
        -s labeling \
        -l xx-labeling # Specify the labeling directory (without labeling/)
    ```

4. Start the sync server 
    ```bash
    screen -r labeling-sync
    cd scripts 
    bash ./0-dropbox-sync.sh xx-labeling xx-dropbox-dir
    ```
    Please note: 
    - The `xx-dropbox-dir` is the path after `home/` in a dropbox link. For example, if you have a dropbox folder link like: `https://www.dropbox.com/home/Label-Studio-Labeling/2010_test`, the `xx-drop-dir` is then `Label-Studio-Labeling/2010_test`. 
    
    - You may want to create the folder on dropbox before you start the sync process. 

## Create the model prediction server 

1. Obtain the model configuration and weights file paths. Normally they are stored on Dropbox. And you can directly click share for the individual files to obtain shared links like 
    - `https://www.dropbox.com/s/<>/config.yaml?dl=1` for `config_path` 
    - `https://www.dropbox.com/s/<>/model_final.pth?dl=1` for `model_path`

2. Replace the `config_path` and `model_path` in the `tools/model.py` file in [line 77](https://github.com/dell-research-harvard/labeling-toolkit-template/blob/8100c051458e559739f2ac4826b23c316af05976/tools/model.py#L77) or the `tools/model_al.py` file.

3. Ensure the [`label_map`](https://github.com/dell-research-harvard/labeling-toolkit-template/blob/8100c051458e559739f2ac4826b23c316af05976/tools/model.py#L81) is correct for the given dataset: 
   1. The model will generate the predictions in numerical format, but label-studio only accepts string format of the labels. You need to manually specify the way to convert between the numerical format and string format of the labels. 

### Plain model prediction server  

1. Generate the modeling server via: 
    ```bash
    cd scripts
    bash ./3-create-modeling-server.sh \
        -s model.py \
        -t xx-labeling-backend 
    ```

2. Start the modeling server via:

    ```bash
    cd scripts
    bash ./4-start-modeling-server.sh \
        -s modeling \
        -m xx-labeling-backend 
    ```

### AL model prediction server 

1. Replace the `config_path` and `model_path` in the `tools/model_al.py` file in [line 77](https://github.com/dell-research-harvard/labeling-toolkit-template/blob/8100c051458e559739f2ac4826b23c316af05976/tools/model.py#L77).

1. Generate the modeling server via: 
    ```bash
    cd scripts
    bash ./3-create-modeling-server.sh \
        -s model_al.py \
        -t xx-labeling-backend-al
    ```

2. Start the modeling server via:

    ```bash
    cd scripts
    bash ./4-start-modeling-server.sh \
        -s modeling-al \
        -m xx-labeling-backend-al 
    ```

## Export the dataset and start training 

1. Export the labeled samples and create a COCO dataset 

    ```bash
        cd scripts
        bash ./5-export-dataset.sh -e export -l xx-labeling
    ```

2. You can then transfer it to another model training servers, and use this dataset to train a new deep layout detection model. 