#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

echo 'This script will create and populate a local mysql db for use in'
echo 'demonstrating the database schema import capbilities on Tigergraph'
echo ''
echo ' Run this command to ensure the user can login by providing a pw'
echo ''
echo '   mysql -ubob -p'
echo ''
echo ' for user bob, and supplying their password, login is successful.'
echo ''
echo " Running on ${OSTYPE}"
echo ''

./scripts/checkServerStatus.sh
retVal=$?

if [[ "$retVal" == 2 ]]; then
	echo 'mysql doesnt appear to be installed or running, please address'
	echo ''
	exit 2
fi

echo ''
read -p "Username: " userName
echo ''
read -s -p "Password: " pw
echo ''

echo "Install IMDB schema"
echo ''
mysql -u${userName} -p${pw} < ./imdb/scripts/createIMDBSchema.sql
echo "Install Synthea schema"
echo ''
mysql -u${userName} -p${pw} < ./synthea/scripts/createSyntheaSchema.sql
echo "Install LDBC schema"
echo ''
mysql -u${userName} -p${pw} < ./ldbc/scripts/createLDBCSchema.sql
echo "Install Airline schema"
echo ''
mysql -u${userName} -p${pw} < ./airline/scripts/createAirlineSchema.sql
echo "Install Recommendations schema"
echo ''
mysql -u${userName} -p${pw} < ./recommendations/scripts/createRecommendationsSchema.sql
echo ''
read -p "Do you also want to load data for each database? (Y/y or N/n): " loadData

if [[ "$loadData" == "Y" || "$loadData" == "y" ]]; then
	echo ''
    echo "lets do it"

	mysql --local-infile=1 -uroot -p${pw} < ./imdb/scripts/loadIMDBDataSamples.sql
	mysql --local-infile=1 -uroot -p${pw} < ./synthea/scripts/loadSyntheaData.sql
	mysql --local-infile=1 -uroot -p${pw} < ./ldbc/scripts/loadLDBCDataSample.sql
	mysql --local-infile=1 -uroot -p${pw} < ./airline/scripts/loadAirlineData.sql
	mysql --local-infile=1 -uroot -p${pw} < ./recommendations/scripts/loadRecommendationsData.sql

else
	echo ''
    echo "ok, maybe later"
fi


