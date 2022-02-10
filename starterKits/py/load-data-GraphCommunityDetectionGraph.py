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
   
USE GRAPH GraphCommunityDetectionGraph

GRANT DATA_SOURCE tg_s3_data_source TO GRAPH GraphCommunityDetectionGraph

CREATE LOADING JOB GraphCommunityDetectionGraph_load_job FOR GRAPH GraphCommunityDetectionGraph {

LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/Specialty.tsv\'}" TO VERTEX Specialty VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/SubSpecialty.tsv\'}" TO VERTEX SubSpecialty VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/Claim.tsv\'}" TO VERTEX Claim VALUES ($"primary_id", $"rx_fill_date", $"ICD10Code", $"ICD10CodeDescription", $"CodeGroupTitle") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/Patient.tsv\'}" TO VERTEX Patient VALUES ($"primary_id") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/Prescriber.tsv\'}" TO VERTEX Prescriber VALUES ($"primary_id", $"pageRank", $"communityId") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/Kangaroo.tsv\'}" TO VERTEX Kangaroo VALUES ($"primary_id", $"communityId") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/FlickrImage.tsv\'}" TO VERTEX FlickrImage VALUES ($"primary_id", $"communityId") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/associated.tsv\'}" TO EDGE associated VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/specialty_subspecialty.tsv\'}" TO EDGE specialty_subspecialty VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/submitted_by.tsv\'}" TO EDGE submitted_by VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/subspecialty_prescriber.tsv\'}" TO EDGE subspecialty_prescriber VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/referral.tsv\'}" TO EDGE referral VALUES ($"from", $"to", $"num_patient") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/kanga_link.tsv\'}" TO EDGE kanga_link VALUES ($"from", $"to", $"weight") USING SEPARATOR = "\\t", HEADER = "true";
LOAD "$tg_s3_data_source:{\'file.uris\':\'s3://tg-workshop-us/starter-kits/GraphCommunityDetection/flickr_link.tsv\'}" TO EDGE flickr_link VALUES ($"from", $"to") USING SEPARATOR = "\\t", HEADER = "true";
}

RUN LOADING JOB GraphCommunityDetectionGraph_load_job USING EOF="true"
DROP JOB GraphCommunityDetectionGraph_load_job
''', options=[]))
