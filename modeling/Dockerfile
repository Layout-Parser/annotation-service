# Building the main container
FROM python:3.8-slim

# Add arguments
ARG MODEL_CONFIG
ENV MODEL_CONFIG=${MODEL_CONFIG}
ARG MODEL_WEIGHTS
ENV MODEL_WEIGHTS=${MODEL_WEIGHTS}
ARG LABEL_MAP
ENV LABEL_MAP=${LABEL_MAP}
ARG GPU
ENV GPU=${GPU:-}

# Set working directory
WORKDIR /annotation-service-modeling

# Update
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install ffmpeg libsm6 libxext6 -y

# Copy and install requirements.txt first for caching
COPY requirements.txt /annotation-service-modeling
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN if [[ -z "$GPU" ]] ; \
    then \
    python -m pip install detectron2 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.5/index.html ; \
    else \
    python -m pip install detectron2 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.5/index.html ; \
    fi
# TODO !!! BOTH CPU, CHANGE THIS

COPY ./src/label-studio /annotation-service-modeling/src/label-studio
RUN cd ./src/label-studio && pip install -e .
RUN cd ./src/label-studio/label_studio/ml/examples && pip install -r requirements.txt

# basic env vars
ENV PORT="9090"
ENV PROJECT_NAME="modeling-backend"
ENV HOST=0.0.0.0
ENV PROTOCOL=http://

# basic auth params
ENV USERNAME=""
ENV PASSWORD=""

# expose port
EXPOSE ${PORT}

# copy from modeling
COPY ./src/label-studio /annotation-service-modeling
COPY modeling /annotation-service-modeling

# init
#RUN label-studio-ml init modeling-backend \
#    --script tools/model.py \
#    --force

# start
# CMD ["label-studio-ml", "start", "modeling-backend"]