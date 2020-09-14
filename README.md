# Labeling Toolkit Template

You can download this tool via:

```bash
git clone --recurse-submodules -j8 git@github.com:dell-research-harvard/labeling-toolkit-template.git
```

## Steps for using this tool

1. Create your data downloading, sampling and conversion script and add to the `tools` or `scripts` folder.

2. Install the label-studio tool via: 

    ```bash
    cd src/label-studio
    pip install -U -e .
    ```

3. Create the labeling project via

    ```bash
    cd scripts
    bash ./1-create-labeling-server.sh \
        -c horizontal-layout.xml \
        -s data \
        -t xx-labeling # Specify the target directory (without labeling/)
    ```

4. Start the labeling server via 

    ```bash 
    cd scripts
    bash ./2-start-labeling-server.sh \
        -s labeling \
        -l xx-labeling # Specify the labeling directory (without labeling/)
    ```

5. Start the Sync server 
    ```bash
    screen -r labeling-sync
    cd scripts 
    bash ./-dropbox-sync xx-labeling xx-server-addr
    ```