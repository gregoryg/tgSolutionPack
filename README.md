# TigerGraph Solution Kit installer

`tgSolutionPack` - this package contains scripts and data to be used to populate any TigerGraph instance with on of the popular starter kit demos. Currently the kit includes these use cases:

    - Airline data
    - Entity Resolution (MDM)
    - Fraud Detection - TBD
    - LDBC benchmark Data
    - TPC-DS Benchmark - TBD
    - Synthea Health Care data
    - Flight Delays - public transportation dataset - TBD
    - Customer 360 - TBD

The package can be installed on any instance containing a TigerGraph application. The install process is simple:

1.  Copy (scp for secure copy) the tgSolutionPack.tar.gz archive file to the target machine. if you are running Docker locally:

    ```bash
    scp -P 14022 tgSolutionPack.tar.gz tigergraph@localhost:~/
    ```
This will transfer the file to the root of the `tigergraph` user home

2.  SSH to the container

    ```bash
    ssh -p 14022 tigergraph@localhost
    ```

3.  Uncompress the archive to the `mydata` directory:

    ```bash
    mkdir ~/mydata
    cd mydata
    tar -xzvf ../tgSolutionPack.tar.gz
    ```

4.  change directory into the tgSolutionPack folder:

    ```bash
    cd tgSolutionPack
    ```

5.  run the install script and follow the instructions

    ```bash
    ./runDPInstall.sh
    ```

6.  Select one of the solution packs to install

    1 - Entity Resolution(MDM)

    2 - Fraud Detection

    3 - LDBC Benchmark

    4 - TPC-DS Benchmark

    5 - Synthea Healthcare

    6 - Flight Delays

    7 - Customer360

7.  The script Will create the objects, loading job and begin to load data.

8.  Go to the Studio UI to see progress
    -   for the local Docker container: <http://localhost:14240>
