#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## This scripts will create schemas and load data from S3, depending on input

for file in "./"create*
do
  	[[ -f "$file" ]] && echo "Publishing kit $file to the cloud..."

  	echo "Execute the python script"
  	python $file

done

