# Layout Parser Annotation Service

You can launch the annotation service by using Docker Compose to simultaneously start up Label Studio labeling and modeling servers, as below:

```bash
# clone repo
git clone --recurse-submodules git@github.com:Layout-Parser/annotation-service.git
# change working directory to annotation service repo
cd annotation-service
# start labeling and modeling servers
DATA=./data CONFIG=labeling-config.xml MODEL=model.py docker-compose up --build -d
```

In the last command, the environmental variables `DATA`, `CONFIG`, and `MODEL` are used to set the labeling data directory, Label Studio configuration file, and ML backend model file, respectively. (By default, `DATA=./data`, `CONFIG=horizontal-layout.xml`, and `MODEL=model.py`.)

Importantly, the file referenced by `CONFIG` must be located in `annotation-service/labeling/config` and the file referenced by `MODEL` must be located in `annotation-service/modeling/tools`.