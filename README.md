# Layout Parser Annotation Service

## Usage 

We package all the layout annotation service (the annotation interface and active learning modeling server) inside docker containers. The installation process is very straightforward and simple: 

1. Install Docker on your computer, following the [official instructions](https://www.docker.com/get-started).
2. Clone this repository to your computer. 
    ```bash
    git clone --recurse-submodules git@github.com:Layout-Parser/annotation-service.git
    cd annotation-service
    ```
3. Configure the annotation folders (see details in the section below). 
4. Start the docker container
    ```bash
    DATA=./data CONFIG=labeling-config.xml MODEL=model.py docker-compose up --build -d
    ```
5. Go to [localhost:8080](localhost:8080) and start annotating. 
6. Export the completed annotations via Label-Studio's [export function](http://localhost:8080/export), or you can find the annotation folder directly at [`labeled`](./labeled). 

## Configuration

In the last command, the environmental variables `DATA`, `CONFIG`, and `MODEL` are used to set the labeling data directory, Label Studio configuration file, and ML backend model file, respectively. (By default, `DATA=./data`, `CONFIG=horizontal-layout.xml`, and `MODEL=model.py`.)

Importantly, the file referenced by `CONFIG` must be located in `annotation-service/labeling/config` and the file referenced by `MODEL` must be located in `annotation-service/modeling/tools`.