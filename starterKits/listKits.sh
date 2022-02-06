#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This scripts will create schemas and load data from S3, depending on input

echo ''
echo "The tgSolutionPack includes the following starter kits:"
echo ''

COUNTER=0
for file in "./"kits/*
do
  	if [[ -d "$file" ]]; then
  		echo "   $file"
		COUNTER=$(( COUNTER + 1 ))
	fi
done

echo ''
echo "There are a total of $COUNTER kits"
echo

