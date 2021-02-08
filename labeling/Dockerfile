# Building the main container
FROM python:3.8-slim

# Add arguments
ARG IMG_DIR
ARG CONFIG_FILE
ARG GPU
ENV GPU=${GPU:-}

# Set working directory
WORKDIR /annotation-service-labeling

# Update
RUN apt-get update && apt-get install -y build-essential

# Copy and install requirements.txt first for caching
COPY requirements.txt /annotation-service-labeling
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src/label-studio /annotation-service-labeling/src/label-studio
RUN cd ./src/label-studio && pip install -e .

# basic env vars
ENV PORT="8080"
ENV PROJECT_NAME="labeling-frontend"
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
# RUN label-studio init labeling-frontend \
#    --input-path=${IMG_DIR} \
#    --input-format=image-dir \
#    --allow-serving-local-files --force \
#    --label-config=configs/${CONFIG_FILE} \
#    --port ${PORT} \
#    --ml-backends http://localhost:9090

# Start server
# ENTRYPOINT [ "label-studio", "start", "labeling-frontend"]