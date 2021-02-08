FROM python:3.8-slim
WORKDIR /testing-modeling
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y git

RUN pip install torch torchvision
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
COPY requirements2.txt /testing-modeling
RUN pip install -r requirements2.txt
RUN pip install git+https://github.com/heartexlabs/label-studio.git
RUN pip install -U 'git+https://github.com/facebookresearch/fvcore'

COPY configs /testing-modeling/configs

EXPOSE 9090

RUN label-studio-ml init labeling/var_backend \
    --script configs/model.py --force

# CMD label-studio-ml start labeling/var_backend --port 9090