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
DROP GRAPH InDBMLGraph

CREATE GRAPH InDBMLGraph()
USE GRAPH InDBMLGraph

CREATE SCHEMA_CHANGE JOB InDBMLGraph_change_job FOR GRAPH InDBMLGraph {

ADD VERTEX USER(PRIMARY_ID user_id STRING, theta LIST<DOUBLE>) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX MOVIE(PRIMARY_ID movie_id STRING, name STRING, avg_rating DOUBLE, x LIST<DOUBLE>) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE rate(FROM USER, TO MOVIE, rating DOUBLE, label BOOL DEFAULT "TRUE");
}

RUN SCHEMA_CHANGE JOB InDBMLGraph_change_job
DROP JOB InDBMLGraph_change_job
''', options=[])
