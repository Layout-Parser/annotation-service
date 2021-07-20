FROM python:3.8-slim

WORKDIR /annotation_service_modeling

RUN apt-get update && apt-get install -y build-essential
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y git

COPY requirements.txt .
RUN pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
RUN pip install -U detectron2==0.1.1 -f \
    https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.4/index.html
RUN pip install git+https://github.com/Layout-Parser/label-studio.git

COPY tools tools/

EXPOSE 9090