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
   
USE GRAPH CommunityDetectionGraph

CREATE LOADING JOB CommunityDetectionGraph_load_job FOR GRAPH CommunityDetectionGraph {

LOAD "ANY:$sys.data_root/GlobalTypes/Specialty.csv" TO VERTEX Specialty VALUES ($"primary_id") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/SubSpecialty.csv" TO VERTEX SubSpecialty VALUES ($"primary_id") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/Claim.csv" TO VERTEX Claim VALUES ($"primary_id", $"rx_fill_date", $"ICD10Code", $"ICD10CodeDescription", $"CodeGroupTitle") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/Patient.csv" TO VERTEX Patient VALUES ($"primary_id") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/Prescriber.csv" TO VERTEX Prescriber VALUES ($"primary_id", $"pageRank", $"communityId") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/Kangaroo.csv" TO VERTEX Kangaroo VALUES ($"primary_id", $"communityId") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/FlickrImage.csv" TO VERTEX FlickrImage VALUES ($"primary_id", $"communityId") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/associated.csv" TO EDGE associated VALUES ($"from", $"to") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/specialty_subspecialty.csv" TO EDGE specialty_subspecialty VALUES ($"from", $"to") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/submitted_by.csv" TO EDGE submitted_by VALUES ($"from", $"to") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/subspecialty_prescriber.csv" TO EDGE subspecialty_prescriber VALUES ($"from", $"to") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/referral.csv" TO EDGE referral VALUES ($"from", $"to", $"num_patient") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/kanga_link.csv" TO EDGE kanga_link VALUES ($"from", $"to", $"weight") USING SEPARATOR = "", HEADER = "true";
LOAD "ANY:$sys.data_root/GlobalTypes/flickr_link.csv" TO EDGE flickr_link VALUES ($"from", $"to") USING SEPARATOR = "", HEADER = "true";
}
}

RUN LOADING JOB CommunityDetectionGraph_change_job
DROP JOB CommunityDetectionGraph_change_job
''', options=[]))
