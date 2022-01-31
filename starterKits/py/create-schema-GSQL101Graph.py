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
host = "https://mov-rec-tgws.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH GSQL101Graph

CREATE GRAPH GSQL101Graph()
USE GRAPH GSQL101Graph

CREATE SCHEMA_CHANGE JOB GSQL101Graph_change_job FOR GRAPH GSQL101Graph {

ADD VERTEX person(PRIMARY_ID name STRING, name STRING, age INT, gender STRING, state STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD UNDIRECTED EDGE friendship(FROM person, TO person, connect_day DATETIME);
}

RUN SCHEMA_CHANGE JOB GSQL101Graph_change_job
DROP JOB GSQL101Graph_change_job
''', options=[])
