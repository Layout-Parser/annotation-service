FROM python:3.8-slim

WORKDIR /annotation_service_modeling

RUN apt-get update && apt-get install -y build-essential
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y git

RUN pip install torch torchvision
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
COPY requirements.txt /annotation_service_modeling
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/heartexlabs/label-studio.git
RUN pip install -U 'git+https://github.com/facebookresearch/fvcore'

COPY tools /annotation_service_modeling/tools

EXPOSE 9090