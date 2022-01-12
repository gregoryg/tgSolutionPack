#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## Check if gadmin is installed
command -v gadmin >/dev/null 2>&1 || { echo >&2 "TigerGraph is not installed  Aborting."; exit 1; }

## ensure tg is running and gsql is available
resp=$(gsql -v)
if [[ "$resp" == *"refused"* || "$resp" == *"not found"* ]]; then
    echo "Tigergraph does not appear to be running here."
    exit 0
fi

echo ''
echo "TigerGraph tgSolutionPack install script"
echo ""
echo "Usage: "
echo ""
echo "1 - Entity Resolution(MDM)"
echo "2 - Fraud Detection"
echo "3 - LDBC Benchmark"
echo "4 - TPC-DS Benchmark"
echo "5 - Synthea HealthCare"
echo '6 - IMDB'
echo "7 - Customer360"
echo '8 - Recommendations'
echo '9 - AML Sim'
echo '10 - Ontime Flight Performance'
echo '11 - Adworks'
echo "A/a - install all of the packs"
echo "mysql - Stage all of the source data to a local mysql db"
echo ''

read -p "Pick a number, or enter a/A for all: " choice

echo "You selected $choice to install, is this correct?"

case $choice in

	1)
		echo ''
		echo "Install MDM...."
		gsql packages/entityResMDM/scripts/01-create-schema.gsql
		gsql packages/entityResMDM/scripts/02-load-data.gsql
		gsql packages/entityResMDM/scripts/03-add-queries.gsql
	    ;;
	2)
	    echo "Install Fraud/AML"
		gsql packages/fraud/scripts/01-create-schema.gsql
		gsql packages/fraud/scripts/02-load-data.gsql
	    ;;
	3)
		echo ''
		echo "Install LDBC - with small sample dataset"
		gsql packages/ldbc/scripts/01-create-schema.gsql
		gsql packages/ldbc/scripts/02-load-data-sample.gsql
	    ;;
	4)
	    echo ''
	    echo "Install TPC-DS"
		gsql packages/tpcds/scripts/01-create-schema.gsql
		gsql packages/tpcds/scripts/02-load-data.gsql
	    ;;
	5)
	    echo ''
	    echo "Install Synthea"
		gsql packages/synthea/scripts/createSyntheaSchema.gsql
		./packages/synthea/scripts/installLoadJobs.sh
		gsql packages/synthea/scripts/runSyntheaLoadJobs.gsql
	    ;;
	6)
	    echo ''
	    echo "Install IMDB"
	    gsql packages/imdb/scripts/01-create-schema.gsql
	    gsql packages/imdb/scripts/02-load-data.gsql
	    ;;
	7)
	    echo ''
	    echo "Install Cust360"
	    ./packages/cust360/installCust360.sh
	    ;;
	8)
	    echo ''
	    echo "Install Recommendations"
		gsql packages/recommendations/scripts/01-create-schema.gsql
		gsql packages/recommendations/scripts/02-load-data.gsql
	    ;;
	9)
	    echo ''
	    echo "Install AML Sim"
		gsql work-in-progress/AMLSim/scripts/01-create-schema.gsql
		gsql work-in-progress/AMLSim/scripts/02-load-data.gsql
	    ;;
	10)
	    echo ''
	    echo "Install Ontime Perf Graph"
		gsql work-in-progress/airline/scripts/01-create-schema.gsql
		gsql work-in-progress/airline/scripts/createAirlineLoadJobs.gsql
	    ;;
	11)
	    echo ''
	    echo "Install Adworks Graph"
		gsql work-in-progress/adworks/scripts/01-create-schema.gsql
	    ;;

	a)
	    echo ''
	    echo 'Lets load all of the schemas'
		gsql packages/entityResMDM/scripts/01-create-schema.gsql
		gsql packages/entityResMDM/scripts/02-load-data.gsql
		gsql packages/entityResMDM/scripts/03-add-queries.gsql
	    echo "Install Fraud/AML - data tbd"
		gsql packages/fraud/scripts/01-create-schema.gsql
		gsql packages/fraud/scripts/02-load-data.gsql
		echo ''
		echo "Install LDBC - with small sample dataset"
		gsql packages/ldbc/scripts/01-create-schema.gsql
		gsql packages/ldbc/scripts/02-load-data-sample.gsql
	    echo ''
	    echo "Install TPC-DS - data tbd"
		gsql packages/tpc-ds/scripts/01-create-schema.gsql
		gsql packages/tpc-ds/scripts/02-load-data.gsql
	    echo ''
	    echo "Install Synthea"
		gsql packages/synthea/scripts/createSyntheaSchema.gsql
		./packages/synthea/scripts/installLoadJobs.sh
		gsql packages/synthea/scripts/runSyntheaLoadJobs.gsql
	    echo ''
	    echo "Install IMDB"
	    gsql packages/imdb/scripts/01-create-schema.gsql
	    gsql packages/imdb/scripts/02-load-data.gsql
	    echo ''
	    echo "Install Cust360"
	    ./packages/cust360/installCust360.sh
	    echo ''
	    echo "Install Recommendations"
		gsql packages/recommendations/scripts/01-create-schema.gsql
		gsql packages/recommendations/scripts/02-load-data.gsql
	    echo ''
	    echo "Install AML Sim"
		gsql work-in-progress/AMLSim/scripts/01-create-schema.gsql
		gsql work-in-progress/AMLSim/scripts/02-load-data.gsql
	    echo "Install Ontime Perf Graph"
		gsql work-in-progress/airline/scripts/01-create-schema.gsql
		gsql work-in-progress/airline/scripts/createAirlineLoadJobs.gsql
	    echo ''
	    echo "Install Adworks Graph"
		gsql work-in-progress/adworks/scripts/01-create-schema.gsql
	    echo ''
	    ;;
	mysql)
	    echo ''
	    echo 'Lets stage all of the schemas to mysql'
	    echo ''
	    ./runMySQLSetup.sh
	    echo ''
esac

echo ''
echo 'Finished with setup....'
