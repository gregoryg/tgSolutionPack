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
   
USE GRAPH ConvolNetworkGraph

CREATE LOADING JOB ConvolNetworkGraph_load_job FOR GRAPH ConvolNetworkGraph {

LOAD "ANY:$sys.data_root/GlobalTypes/PAPER.csv" TO VERTEX PAPER VALUES ($"primary_id", $"indx", SPLIT($"words", ":", "#"), $"class_label", $"train", $"validation", $"test", $"data_split_label") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/WORD.csv" TO VERTEX WORD VALUES ($"primary_id", $"indx") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/LAYER_0.csv" TO VERTEX LAYER_0 VALUES ($"primary_id", $"indx") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/LAYER_1.csv" TO VERTEX LAYER_1 VALUES ($"primary_id", $"indx") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/CITE.csv" TO EDGE CITE VALUES ($"from", $"to", $"weight") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/HAS.csv" TO EDGE HAS VALUES ($"from", $"to", $"weight") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/WORD_LAYER_0.csv" TO EDGE WORD_LAYER_0 VALUES ($"from", $"to", $"weight") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/LAYER_0_LAYER_1.csv" TO EDGE LAYER_0_LAYER_1 VALUES ($"from", $"to", $"weight") USING SEPARATOR = "", HEADER = "true";
}
}

RUN LOADING JOB ConvolNetworkGraph_change_job
DROP JOB ConvolNetworkGraph_change_job
''', options=[]))
