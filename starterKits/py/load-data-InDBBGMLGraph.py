#!/usr/bin/env python
# coding: utf-8

# # 1 - TigerGraph Schema Refresh Job
# 
# This script is used to automatically refresh the Stanza TigerGraph instance on TGCloud
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Create load jobs
#     4. Run load jobs
# 


# FETCH PACKAGES
import subprocess
import sys

import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# 
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "https://tg-se-demo-hub.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123" 

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# Create load jobs

print(conn.gsql('''
   
USE GRAPH InDBBGMLGraph

GRANT DATA_SOURCE tg_s3_data_source TO GRAPH InDBBGMLGraph

CREATE LOADING JOB InDBBGMLGraph_load_job FOR GRAPH InDBBGMLGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Last_Name.tsv\'}" TO VERTEX Last_Name VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Email.tsv\'}" TO VERTEX Email VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Phone.tsv\'}" TO VERTEX Phone VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/IP.tsv\'}" TO VERTEX IP VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Device.tsv\'}" TO VERTEX Device VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Video_Play_Event.tsv\'}" TO VERTEX Video_Play_Event VALUES ($"primary_id", $"play_time", $"play_duration") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Video.tsv\'}" TO VERTEX Video VALUES ($"primary_id", $"runtime", $"title", $"release_date") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Genre.tsv\'}" TO VERTEX Genre VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Keyword.tsv\'}" TO VERTEX Keyword VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/address.tsv\'}" TO VERTEX address VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User.tsv\'}" TO VERTEX User VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Account.tsv\'}" TO VERTEX Account VALUES ($"primary_id", $\'first_name", $"middle_name", $"last_name", $"gender", $"dob") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Play_Video.tsv\'}" TO EDGE Play_Video VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Genre.tsv\'}" TO EDGE Has_Genre VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Keyword.tsv\'}" TO EDGE Has_Keyword VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User_IP.tsv\'}" TO EDGE User_IP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User_Email.tsv\'}" TO EDGE User_Email VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User_LastName.tsv\'}" TO EDGE User_LastName VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User_Phone.tsv\'}" TO EDGE User_Phone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User_Address.tsv\'}" TO EDGE User_Address VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/User_Device.tsv\'}" TO EDGE User_Device VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_IP.tsv\'}" TO EDGE Has_IP VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Email.tsv\'}" TO EDGE Has_Email VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Last_Name.tsv\'}" TO EDGE Has_Last_Name VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Device.tsv\'}" TO EDGE Has_Device VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Play_Event.tsv\'}" TO EDGE Has_Play_Event VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Phone.tsv\'}" TO EDGE Has_Phone VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Address.tsv\'}" TO EDGE Has_Address VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/Has_Account.tsv\'}" TO EDGE Has_Account VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/InDBBGML/SameAs.tsv\'}" TO EDGE SameAs VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}

RUN LOADING JOB InDBBGMLGraph_load_job USING EOF="true"
DROP JOB InDBBGMLGraph_load_job
''', options=[]))
