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
   
USE GRAPH COVID19Graph

GRANT DATA_SOURCE tg_s3_data_source TO GRAPH COVID19Graph

CREATE LOADING JOB COVID19Graph_load_job_country FOR GRAPH COVID19Graph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/COVID19/country2.csv\'}" TO VERTEX Country VALUES ($"primary_id", $"country") USING SEPARATOR = "\\t", HEADER = "true";
}

RUN LOADING JOB COVID19Graph_load_job_country USING EOF="true"
''', options=[]))
