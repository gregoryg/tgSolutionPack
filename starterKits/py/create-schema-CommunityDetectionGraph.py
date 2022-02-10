#!/usr/bin/env python

# # 1 - TigerGraph Schema Refresh Job
# 
# These scripts are used to automatically refresh the a TigerGraph instance on TGCloud (or EC2)
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Run schema change job
#     3. Create load jobs
#     4. Run load jobs
# 

# FETCH PACKAGES
import sys
import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "https://tg-se-demo-hub.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH CommunityDetectionGraph

CREATE GRAPH CommunityDetectionGraph()
USE GRAPH CommunityDetectionGraph

CREATE SCHEMA_CHANGE JOB CommunityDetectionGraph_change_job FOR GRAPH CommunityDetectionGraph {

ADD VERTEX Specialty(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX SubSpecialty(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Claim(PRIMARY_ID Claim_id STRING, rx_fill_date DATETIME, ICD10Code STRING, ICD10CodeDescription STRING, CodeGroupTitle STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Patient(PRIMARY_ID Patient_id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Prescriber(PRIMARY_ID Prescriber_id STRING, pageRank FLOAT, communityId INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX Kangaroo(PRIMARY_ID id STRING, communityId INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX FlickrImage(PRIMARY_ID id STRING, communityId INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE associated(FROM Claim, TO Patient) WITH REVERSE_EDGE="reverse_associated";
ADD DIRECTED EDGE specialty_subspecialty(FROM Specialty, TO SubSpecialty) WITH REVERSE_EDGE="reverse_specialty_subspecialty";
ADD DIRECTED EDGE submitted_by(FROM Claim, TO Prescriber) WITH REVERSE_EDGE="reverse_submitted_by";
ADD DIRECTED EDGE subspecialty_prescriber(FROM SubSpecialty, TO Prescriber) WITH REVERSE_EDGE="reverse_subspecialty_prescriber";
ADD DIRECTED EDGE referral(FROM Prescriber, TO Prescriber, num_patient INT DEFAULT "0") WITH REVERSE_EDGE="reverse_referral";
ADD UNDIRECTED EDGE kanga_link(FROM Kangaroo, TO Kangaroo, weight FLOAT);
ADD UNDIRECTED EDGE flickr_link(FROM FlickrImage, TO FlickrImage);
}

RUN SCHEMA_CHANGE JOB CommunityDetectionGraph_change_job
DROP JOB CommunityDetectionGraph_change_job
''', options=[])
