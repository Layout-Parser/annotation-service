FROM python:3.8-slim

WORKDIR /annotation_service_labeling

RUN apt-get update && apt-get install -y build-essential
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y git

COPY requirements.txt /annotation_service_labeling
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/Layout-Parser/label-studio.git

COPY configs /annotation_service_labeling/configs

EXPOSE 8080