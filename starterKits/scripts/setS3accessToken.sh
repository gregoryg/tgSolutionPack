#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## Get TG connection info


#sed "s/HOSTTOKEN/${tg_host}/g" ./templates/tg_createLoadJob_template.py.orig > bob.tmp

#mv bob3.tmp ./templates/tg_createLoadJob_template.py

echo ''
echo 'Configure the S3 access token'
echo ''

read -p "Path to access file file, and filename: " tokenFile

while IFS= read -r line
do
  echo "$line"
  if [[ $line == *"Access"* ]];
then
    continue
else
    arrIN=(${line//,/ })
    echo ${arrIN[1]}  
    access_key_id=${arrIN[0]}
    secret_access_key=${arrIN[1]}
fi
done < "$tokenFile"

## add the keys to the load job template
sed "s/ACCESSKEYID/${access_key_id}/g" ./templates/tg_createLoadJob_template.py.orig > bob.tmp
sed "s/SECRETACCESSKEY/${secret_access_key}/g" bob.tmp > ./templates/tg_createLoadJob_template.py
rm -rf bob.tmp
