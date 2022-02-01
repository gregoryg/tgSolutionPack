#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## Get TG connection info

props_file='./scripts/tg.properties'
if [ -f "$props_file" ]
then
  while IFS='=' read -r key value
  do
    key=$(echo $key | tr '.' '_')
    eval ${key}=\${value}
  done < "$props_file"
else
  echo "$file not found, use defaults"
  ## Default to local docker
  tg_host='localhost'
  tg_username="tigergraph"
  tg_password="tigergraph" 
fi

echo 'Enter the connection info for the TigerGraph instance. Hit enter for no change'
echo ''
read -p "tg_host <$tg_host>: " new_host
[[ ! -z $new_host ]] && tg_host=$new_host
echo ''
read -p "tg_username <$tg_username>: " new_username
[[ ! -z $new_username ]] && tg_username=$new_username
echo ''
read -p "tg_password <$tg_password>: " new_password
[[ ! -z $new_password ]] && tg_password=$new_password
echo ''
echo 'NOTE: these credentails will be written to the python load scripts in clear text'
echo ''

echo "Host is: $tg_host"

## Replace tokens in the template with actual values

sed "s/HOSTTOKEN/${tg_host}/g" ./templates/tg_createSchema_template.py.orig > bob.tmp
sed "s/USERNAMETOKEN/${tg_username}/g" bob.tmp > bob2.tmp
sed "s/PASSWORDTOKEN/${tg_password}/g" bob2.tmp > bob3.tmp
mv bob3.tmp ./templates/tg_createSchema_template.py
rm -rf bob.tmp bob2.tmp

sed "s/HOSTTOKEN/${tg_host}/g" ./templates/tg_createLoadJob_template.py.orig > bob.tmp
sed "s/USERNAMETOKEN/${tg_username}/g" bob.tmp > bob2.tmp
sed "s/PASSWORDTOKEN/${tg_password}/g" bob2.tmp > bob3.tmp
mv bob3.tmp ./templates/tg_createLoadJob_template.py
rm -rf bob.tmp bob2.tmp

## Create a current props file
echo "tg_host=$tg_host" > ./scripts/tg.properties
echo "tg_username=$tg_username" >> ./scripts/tg.properties
echo "tg_password=$tg_password" >> ./scripts/tg.properties

echo ''
read -p "Are you deploying to tgCloud, or another server with SSL enabled?: " isHTTPS
echo ''

echo 'Python scripts created'
echo ''