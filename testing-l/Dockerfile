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

COPY configs /testing-labeling/configs

EXPOSE 8080