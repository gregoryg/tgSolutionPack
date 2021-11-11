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
echo "6 - Flight Delays"
echo '7 - IMDB'
echo "8 - Customer360"
echo '9 - Recommendations'
echo "A/a - install all of the packs"
echo "mysql - Stage all of the source data to a local mysql db"
echo ''

read -p "Pick a number, or enter a/A for all: " choice

echo "You selected $choice to install, is this correct?"

case $choice in

	1)
		echo ''
		echo "Install MDM...."
		gsql < entityResMDM/createMDMSchema.gsql
		gsql < entityResMDM/createMDMJobs.gsql
		gsql < entityResMDM/runMDMJobs.gsql
	;;
	2)
	echo "Install Fraud/AML - TBD"
	;;
	3)
		echo ''
		echo "Install LDBC - TBD"
		gsql < ldbc/createLDBCSchema.gsql
		gsql < ldbc/createLDBCSampleJobs.gsql
		gsql < ldbc/runLDBCLoadJob.gsql
	;;
	4)
	echo ''
	echo "Install TPC-DS - TBD"
	;;
	5)
	echo ''
	echo "Install Synthea"
		gsql < synthea/scripts/createSyntheaSchema.gsql
		./synthea/scripts/installLoadJobs.sh
		gsql < synthea/scripts/runSyntheaLoadJobs.gsql
	;;
	6)
	echo ''
	echo "Install Flight Delays - TBD"
	 gsql < airline/scripts/createAirlineSchema.gsql
	;;
	7)
	echo ''
	echo "Install IMDB"
	  gsql < imdb/scripts/createIMDBSchema.gsql
	;;
	8)
	echo ''
	echo "Install Cust360 - TBD"
	;;
	8)
	echo ''
	echo "Install Recommendations"
		gsql < recommendations/scripts/createRecommendationsSchema.gsql
	;;
	a)
	echo ''
	echo 'Lets load all of the schemas'
	  gsql < entityResMDM/createMDMSchema.gsql
	  gsql < ldbc/createLDBCSchema.gsql
	  gsql < synthea/scripts/createSyntheaSchema.gsql
	  gsql < airline/scripts/createAirlineSchema.gsql
	  gsql < fraud/scripts/createFraudSchema.gsql
	  gsql < imdb/scripts/createIMDBSchema.gsql
		gsql < recommendations/scripts/createRecommendationsSchema.gsql
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


