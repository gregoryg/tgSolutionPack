# TigerGraph Solution Kit installer

`tgSolutionPack` - this package contains scripts and data to be used to populate any TigerGraph instance with on of the popular starter kit demos. Currently the kit includes these use cases:

<ol>
<li>Entity Resolution(MDM)</li>
<li>Fraud Detection</li>
<li>LDBC Benchmark</li>
<li>TPC-DS Benchmark</li>
<li>Synthea HealthCare</li>
<li>IMDB</li>
<li>Customer360</li>
<li>Recommendations</li>
<li>AML Sim</li>
<li>Ontime Flight Performance</li>
<li>Adworks</li>
</ol>

The tgSolutionPack consists of 2 gzip archieve files for deployment
   
    - tgSolutionPack.tar.gz - contains all of the scripting necessary to deploy
    - tgSolutionPackData.tar.gz - contains the source data for each demo - packaged separately due to large size

1. Clone this project, which contains the tgSolutionPack.tar.gz package

2.  Download the data file archieve using the follwoing command. Note: this public S3 bucket location may change some day

    ```bash
    wget https://tgsedemodatabucket.s3.amazonaws.com/tgSolutionPackData.tar.gz
    ```

The package can be installed on any instance running a TigerGraph application. The install process is simple:

3.  Copy (scp for secure copy) the tgSolutionPack.tar.gz archive file to the target machine. if you are running Docker locally:

    ```bash
    scp -P 14022 tgSolutionPack.tar.gz tigergraph@localhost:~/
    scp -P 14022 tgSolutionPackData.tar.gz tigergraph@localhost:~/
    ```
This will transfer the file to the root of the `tigergraph` user home

4.  SSH to the container

    ```bash
    ssh -p 14022 tigergraph@localhost
    ```

5.  Uncompress the archive to the `mydata` directory:

    ```bash
    mkdir ~/mydata
    cd mydata
    tar -xzvf ../tgSolutionPack.tar.gz
    tar -xzvf ../tgSolutionPackData.tar.gz
    ```

6.  change directory into the tgSolutionPack folder:

    ```bash
    cd tgSolutionPack
    ```

7.  run the install script and follow the instructions

    ```bash
    ./runDPInstall.sh
    ```

8.  Select one of the solution packs to install

    1 - Entity Resolution(MDM)
    2 - Fraud Detection
    3 - LDBC Benchmark
    4 - TPC-DS Benchmark
    5 - Synthea HealthCare
    6 - IMDB
    7 - Customer360
    8 - Recommendations
    9 - AML Sim
    10 - Ontime Flight Performance
    11 - Adworks
    A/a - install all of the packs
    mysql - Stage all of the source data to a local mysql db

9.  The script Will create the objects, loading job and execute each load job to populate the graph.

10.  Go to the Studio UI to see progress
    -   for the local Docker container: <http://localhost:14240>

Notes:
    - The demo pack can also install sql-based schema into a local mysql database

