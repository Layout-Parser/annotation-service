# Layout Parser Annotation Service

You can download this tool via:

```bash
git clone --recurse-submodules git@github.com:Layout-Parser/annotation-service.git
```

## Docker

Generate the labeling and  modeling servers via Docker, using the below commands.

You may need to change Docker memory limits with `--memory` flag.

### Create a labeling server

```bash
docker build -f labeling/Dockerfile \
    -t annotation-service:labeling \
    --build-arg IMG_DIR=data \
    --build-arg CONFIG_FILE=horizontal-layout.xml \
    . && \
docker run --rm -p 8080:8080 \
    -t annotation-service:labeling
```

### Create a modeling server

```bash
docker build -f modeling/Dockerfile \
    -t annotation-service:modeling \
    --build-arg MODEL_CONFIG=xxxxx/config.yaml?dl=1 \
    --build-arg MODEL_WEIGHTS=xxxxx/model_final.pth?dl=1 \
    --build-arg LABEL_MAP="0 headline 1 article 2 newspaper_header 3 masthead 4 author 5 photograph 6 image_caption 7 page_number 8 table 9 cartoon_or_advertisement" \
    . && \
docker run --rm -p 9090:9090 \
    -t annotation-service:modeling
```