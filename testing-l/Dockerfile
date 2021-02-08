FROM python:3.8-slim
WORKDIR /testing-labeling
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y git

RUN pip install torch torchvision
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
COPY requirements2.txt /testing-labeling
RUN pip install -r requirements2.txt
RUN pip install git+https://github.com/heartexlabs/label-studio.git

COPY data /testing-labeling/data
COPY configs /testing-labeling/configs

EXPOSE 8080

RUN label-studio init labeling/newspaper_labeling/ \
    --input-path=data --input-format=image-dir \
    --allow-serving-local-files --force \
    --label-config=configs/labeling-config.xml \
    --port 8080 --ml-backends http://host.docker.internal:9090

#CMD label-studio start labeling/newspaper_labeling \
#    --port 8080