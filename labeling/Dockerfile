# Building the main container
FROM python:3.6-slim

# Add arguments
ARG IMG_DIR
ARG CONFIG_FILE
ARG GPU

# Set working directory
WORKDIR /annotation-service-labeling

# Update
RUN apt-get update && apt-get install -y build-essential

# Copy and install requirements.txt first for caching
COPY requirements.txt /annotation-service-labeling
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN if [[ -z "$GPU" ]] ; \
    then \
    python -m pip install detectron2 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.7/index.html ; \
    else \
    python -m pip install detectron2 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cu110/torch1.7/index.html ; \
    fi
COPY ./src/label-studio /annotation-service-labeling/src/label-studio
RUN cd ./src/label-studio && pip install -U -e .

# basic env vars
ENV PORT="8080"
ENV PROJECT_NAME="labeling"
ENV HOST=0.0.0.0
ENV PROTOCOL=http://

# basic auth params
ENV USERNAME=""
ENV PASSWORD=""

# expose port
EXPOSE ${PORT}

# copy from labeling
COPY labeling /annotation-service-labeling

# Create the labeling server
RUN label-studio init ./labeling \
    --input-path=${IMG_DIR} \
    --input-format=image-dir \
    --label-config=configs/${CONFIG_FILE} \
    --port $PORT \
    --ml-backends http://localhost:9090 \
    --allow-serving-local-files \
    --force

# Start server
ENTRYPOINT [ "label-studio", "start", "./labeling" ]