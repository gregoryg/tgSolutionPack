# Contributing

Please fork this repository (github.com/tigergraph/tgSolutionPack) to your own account.  Create a new branch based of of `main` or `master`.  When ready to submit your contributions, generate a PR to be reviewed.

# Principles to follow using this framework

-   Idempotent: graph will install into an existing TG cluster without wiping schema or data
-   (extra credit): generate way to translate solution export file into scripted nondestructive import
-   Every solution needs a README.md with a script - every query needs some examples of successful parameters for the data
-   Make GSQL scripts and loading jobs easily human-readable
    -   e.g. replace column positions with column names
    -   make import file names explicit
-   Make nothing at the Global level - except for use in Multi-graphs
-   Deploy for data loading to `~tigergraph/mydata` directory.  Best practice is to make this directory a symlink to a directory located under `DataRoot` directory on node `m1`. The reason is that when a Docker or Kubernetes container is restarted, data located anywhere outside `DataRoo` may be lost.

    -   Command to find `DataRoot`

        ```bash
        gadmin config get System.DataRoot
        # Alternative using full dump of config
        gadmin config dump | jq -r '.System.DataRoot'
        ```
