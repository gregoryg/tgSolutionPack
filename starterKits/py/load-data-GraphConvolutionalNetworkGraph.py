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
   
USE GRAPH GraphConvolutionalNetworkGraph

GRANT DATA_SOURCE tg_s3_data_source TO GRAPH GraphConvolutionalNetworkGraph

CREATE LOADING JOB GraphConvolutionalNetworkGraph_load_job FOR GRAPH GraphConvolutionalNetworkGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/PAPER.tsv\'}" TO VERTEX PAPER VALUES ($"primary_id", $"indx", SPLIT($"words", ":", "#"), $"class_label", $"train", $"validation", $"test", $"data_split_label") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/WORD.tsv\'}" TO VERTEX WORD VALUES ($"primary_id", $"indx") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/LAYER_0.tsv\'}" TO VERTEX LAYER_0 VALUES ($"primary_id", $"indx") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/LAYER_1.tsv\'}" TO VERTEX LAYER_1 VALUES ($"primary_id", $"indx") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/CITE.tsv\'}" TO EDGE CITE VALUES ($"from", $"to", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/HAS.tsv\'}" TO EDGE HAS VALUES ($"from", $"to", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/WORD_LAYER_0.tsv\'}" TO EDGE WORD_LAYER_0 VALUES ($"from", $"to", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphConvolutionalNetwork/LAYER_0_LAYER_1.tsv\'}" TO EDGE LAYER_0_LAYER_1 VALUES ($"from", $"to", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
}

RUN LOADING JOB GraphConvolutionalNetworkGraph_load_job USING EOF="true"
DROP JOB GraphConvolutionalNetworkGraph_load_job
''', options=[]))
