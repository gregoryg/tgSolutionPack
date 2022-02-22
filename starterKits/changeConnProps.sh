#!/bin/bash

###############################################
# Copyright (c)  2015-now, TigerGraph Inc.
# All rights reserved
# Solution pack for TigerGraph Pre Sales
# Author: robert.hardaway@tigergraph.com
################################################

## Get TG connection info

props_file='./tg.properties'
if [ -f "$props_file" ]
then
  while IFS='=' read -r key value
  do
    key=$(echo $key | tr '.' '_')
    eval ${key}=\${value}
  done < "$props_file"
else
  echo "$file not found, using defaults"
  ## Default to local docker
  tg_host='localhost'
  tg_username="tigergraph"
  tg_password="tigergraph"
  tg_s3_data_source="s3_data_source"
  tg_s3_bucket_name="tg-workshop-us"
  tg_protocol="http"
fi

echo 'Enter the connection info for the TigerGraph instance. Hit enter for no change'
echo ''
read -p "tg_host <$tg_host>: " new_host
if [[ ! -z $new_host ]];
then 
    tg_host_new=$new_host
else
    tg_host_new=$tg_host
fi
echo ''
read -p "tg_username <$tg_username>: " new_username
if [[ ! -z $new_username ]];
then 
    tg_username_new=$new_username
else
    tg_username_new=$tg_username
fi
echo ''
read -p "tg_password <$tg_password>: " new_password
if [[ ! -z $new_password ]];
then 
    tg_password_new=$new_password
else
    tg_password_new=$tg_password
fi
echo ''
read -p "tg_s3_data_source <$tg_s3_data_source>: " new_tg_s3_data_source
if [[ ! -z $new_tg_s3_data_source ]];
then 
    tg_datasource_new=$new_tg_s3_data_source
else
    tg_datasource_new=$tg_s3_data_source
fi
echo ''
echo 'Dont change the bucket name unless the new bucket has been built to contain the datasets'
echo ''
read -p "tg_s3_bucket_name <$tg_s3_bucket_name>: " new_tg_s3_bucket_name
if [[ ! -z $new_tg_s3_data_source ]];
then 
    tg_bucketname_new=$new_tg_s3_bucket_name
else
    tg_bucketname_new=$tg_s3_bucket_name
fi
echo ''
read -p "tg_protocol <$tg_protocol>: " new_tg_protocol
if [[ ! -z $new_tg_protocol ]];
then 
    tg_protocol_new=$new_tg_protocol
else
    tg_protocol_new=$tg_protocol
fi


echo ''
echo 'NOTE: these credentails will be written to the python load scripts in clear text'
echo ''

echo "Host new is: $tg_host_new"
echo "Host is: $tg_host"

echo ''
echo 'Configure the S3 access token'
echo ''

read -p "Enter the path to access key file, and filename: " tokenFile

while IFS=$' \t\r\n' read -r line
do
  echo "$line"
  if [[ $line == *"Access"* ]];
then
    continue
else
    arrIN=(${line//,/ })
    ##echo ${arrIN[1]}  
    access_key_id=${arrIN[0]}
    secret_access_key=${arrIN[1]}
fi
done < "$tokenFile"

## add the keys to the load job template
sed "s/ACCESSKEYID/${access_key_id}/g" ./py/tg_createDataSource.py > bob.tmp
sed 's/SECRETACCESSKEY/${secret_access_key}/g' bob.tmp > ./py/tg_createDataSource.py
rm -rf bob.tmp

echo "update the props filename"
echo "tg_host=$tg_host_new" > ./tg.properties
echo "tg_username=$tg_username_new" >> ./tg.properties
echo "tg_password=$tg_password_new" >> ./tg.properties
echo "tg_s3_data_source=$tg_datasource_new" >> ./tg.properties
echo "tg_s3_bucket_name=$tg_bucketname_new" >> ./tg.properties
echo "tg_protocol=$tg_protocol_new" >> ./tg.properties

## Replace tokens in the template with actual values
for file in "./py/"*.py
  do
    echo "$file"
    sed "s/${tg_host}/${tg_host_new}/g" $file > bob.tmp
    sed "s/${tg_username}/${tg_username_new}/g" bob.tmp > bob2.tmp
    sed "s/${tg_password}/${tg_password_new}/g" bob2.tmp > bob3.tmp
    sed "s/${tg_protocol}/${tg_protocol_new}/g" bob3.tmp > bob4.tmp

    mv bob4.tmp $file
    rm -rf bob*.tmp
  done

echo ''
echo 'Python scripts created'
