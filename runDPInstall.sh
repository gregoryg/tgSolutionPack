#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Demopack for TigerGraph Pre Sales
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
echo "5 - Flight Delays"
echo "5 - Customer360"
echo ''

read -p "Pick a number, or enter a/A for all: " choice

echo "You selected $choice to install, is this correct?"

case $choice in

	1)
		echo "Install MDM...."
		gsql < entityResMDM/createMDMSchema.gsql
		gsql < entityResMDM/createMDMJobs.gsql
		gsql < entityResMDM/runMDMJobs.gsql
	;;
	2)
	echo "Install Fraud/AML - TBD"
	;;
	3)
	echo "Install LDBC - TBD"
		gsql < ldbc/createLDBCSchema.gsql
	;;
	4)
	echo "Install TPC-DS - TBD"
	;;
	5)
	echo "Install Flight Delays - TBD"
	;;
	6)
	echo "Install Cust360 - TBD"
	;;
esac

echo ''
echo 'Finished with setup....'


