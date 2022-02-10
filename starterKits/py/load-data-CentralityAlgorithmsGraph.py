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
   
USE GRAPH CentralityAlgorithmsGraph

CREATE LOADING JOB CentralityAlgorithmsGraph_load_job FOR GRAPH CentralityAlgorithmsGraph {

LOAD "ANY:$sys.data_root/GlobalTypes/Airport.csv" TO VERTEX Airport VALUES ($"primary_id", $"name", $"city", $"country", $"IATA", $"latitude", $"longitude", $"score") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/flight_to.csv" TO EDGE flight_to VALUES ($"from", $"to", $"miles", $"num_flights") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/flight_route.csv" TO EDGE flight_route VALUES ($"from", $"to", $"miles") USING SEPARATOR = "", HEADER = "true";
}
}

RUN LOADING JOB CentralityAlgorithmsGraph_change_job
DROP JOB CentralityAlgorithmsGraph_change_job
''', options=[]))
