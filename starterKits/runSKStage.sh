#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This scripts will create schemas and load data from S3, depending on input

echo 'This installer will create all of the public starter kits on any tg instance'
echo ''
echo 'The steps are:'
echo '   1. Transform the exported starter kit gsql to be run via python'
echo '   2. Translate load script file locations to be S3 specific'
echo '   3. Use pyTigerGraph package to execute py script and populate instance'

## pick the environment
./scripts/setConnProps.sh
./scripts/setS3accessToken.sh

cd kits

for file in "./"*
do
  	if [[ -d "$file" ]] ; then
  		fn=${file:2:100}
  		## Create the gsql schema and load scripts, for each kit
  		./GSQLGen.sh $fn ${fn}Graph
  	fi
done

cd ../gsql

## Create a python file, for each kit
./stageKits.sh create
./stageKits.sh load

cd ../py

./setS3Path.sh

exit 0

./publishKits.sh

echo 'All starter kits staged'
echo ''