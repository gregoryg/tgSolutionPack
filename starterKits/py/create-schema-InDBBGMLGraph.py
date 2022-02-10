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
DROP GRAPH InDBBGMLGraph

CREATE GRAPH InDBBGMLGraph()
USE GRAPH InDBBGMLGraph

CREATE SCHEMA_CHANGE JOB InDBBGMLGraph_change_job FOR GRAPH InDBBGMLGraph {

ADD VERTEX Last_Name(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Email(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Phone(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX IP(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Device(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Video_Play_Event(PRIMARY_ID id STRING, play_time DATETIME, play_duration UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Video(PRIMARY_ID id STRING, runtime UINT, title STRING, release_date DATETIME) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Genre(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Keyword(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX address(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX User(PRIMARY_ID id STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX Account(PRIMARY_ID id STRING, first_name STRING, middle_name STRING, last_name STRING, gender STRING, dob DATETIME) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE Play_Video(FROM Video_Play_Event, TO Video);
ADD UNDIRECTED EDGE Has_Genre(FROM Video, TO Genre);
ADD UNDIRECTED EDGE Has_Keyword(FROM Video, TO Keyword);
ADD UNDIRECTED EDGE User_IP(FROM User, TO IP);
ADD UNDIRECTED EDGE User_Email(FROM User, TO Email);
ADD UNDIRECTED EDGE User_LastName(FROM User, TO Last_Name);
ADD UNDIRECTED EDGE User_Phone(FROM User, TO Phone);
ADD UNDIRECTED EDGE User_Address(FROM User, TO address);
ADD UNDIRECTED EDGE User_Device(FROM User, TO Device);
ADD UNDIRECTED EDGE Has_IP(FROM Account, TO IP);
ADD UNDIRECTED EDGE Has_Email(FROM Account, TO Email);
ADD UNDIRECTED EDGE Has_Last_Name(FROM Account, TO Last_Name);
ADD UNDIRECTED EDGE Has_Device(FROM Account, TO Device);
ADD UNDIRECTED EDGE Has_Play_Event(FROM Account, TO Video_Play_Event);
ADD UNDIRECTED EDGE Has_Phone(FROM Account, TO Phone);
ADD UNDIRECTED EDGE Has_Address(FROM Account, TO address);
ADD UNDIRECTED EDGE Has_Account(FROM User, TO Account);
ADD UNDIRECTED EDGE SameAs(FROM User, TO User);
}

RUN SCHEMA_CHANGE JOB InDBBGMLGraph_change_job
DROP JOB InDBBGMLGraph_change_job
''', options=[])
