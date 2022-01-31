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
DROP GRAPH ConvolNetworkGraph

CREATE GRAPH ConvolNetworkGraph()
USE GRAPH ConvolNetworkGraph

CREATE SCHEMA_CHANGE JOB ConvolNetworkGraph_change_job FOR GRAPH ConvolNetworkGraph {

ADD VERTEX PAPER(PRIMARY_ID paper_id STRING, indx INT, words MAP<INT, DOUBLE>, class_label INT DEFAULT "-1", train BOOL DEFAULT "False", validation BOOL DEFAULT "False", test BOOL DEFAULT "False", data_split_label STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX WORD(PRIMARY_ID word_id STRING, indx INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX LAYER_0(PRIMARY_ID id STRING, indx INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX LAYER_1(PRIMARY_ID id STRING, indx INT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE CITE(FROM PAPER, TO PAPER, weight DOUBLE);
ADD UNDIRECTED EDGE HAS(FROM PAPER, TO WORD, weight DOUBLE DEFAULT "1.0");
ADD UNDIRECTED EDGE WORD_LAYER_0(FROM WORD, TO LAYER_0, weight DOUBLE DEFAULT "0");
ADD UNDIRECTED EDGE LAYER_0_LAYER_1(FROM LAYER_0, TO LAYER_1, weight DOUBLE);
}

RUN SCHEMA_CHANGE JOB ConvolNetworkGraph_change_job
DROP JOB ConvolNetworkGraph_change_job
''', options=[])
