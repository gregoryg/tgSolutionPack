#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This scripts will create schemas and load data from S3, depending on input

## pick the environment
./scripts/setConnProps.sh

cd kits

for file in "./"*
do
  	if [[ -d "$file" ]] ; then
  		echo "directory: $file"
  		fn=${file:2:100}
  		## Create the gsql schema and load scripts, for each kit
  		./GSQLGen.sh $fn ${fn}Graph
  	fi
done

cd ../gsql

## Create a python file, for each kit
./stageKits.sh create

cd ../py
./publishKits.sh

echo 'All starter kits staged'
echo ''